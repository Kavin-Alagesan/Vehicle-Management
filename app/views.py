from django.shortcuts import render,redirect
from django.contrib import messages
import requests
from django.conf import settings
import json
from django.contrib.auth import logout
from django.http import HttpResponse

url = settings.URL 

# Create your views here.
def user_register(request):
    if request.method == 'POST':
        username =  request.POST['txtUsername']
        email =  request.POST['txtEmail']
        password1 = request.POST.get('txtPwd1')
        password2 = request.POST.get('txtpwd2')

        if password1 == password2:
            data = {
                'username' : username, 
                'email' : email, 
                'password' : password1
                }
            response = requests.post('{url}create_user/'.format(url=url) ,data=data) 
            print(response.text)
            get_response = response.json()
            print('--------------------------register post----------------------------')
            if response.status_code > 300:
                print('--------------------------response>300----------------------------')
                messages.error(request,'Fill empty fields')
                return render(request,'user/register.html',{'response':get_response})
            else:
                messages.success(request,("User created successfully. Wait till admin to assign your ROLE"))
                return redirect('user_signin')
        else:
            return render (request,'user/register.html')
    else:
        return render(request,'user/register.html')

def user_signin(request):
    try:
        if request.method == 'POST':
            username =  request.POST['txtUsername']
            password =  request.POST['txtPwd']
            data={
                'username':username,
                'password':password,   
            }
            response = requests.post('{url}login/'.format(url=url) ,data=data) 
            print(response.text)
            get_response=response.json()
            if response.status_code >= 200 <= 201:
                print('-=-=-=-=logged in 200-=-=-==-')
                print(response.text)
                dict=json.loads(response.text) 
                Token=(dict["access"])
                user_role=(dict["role"])
                print(Token)
                print(user_role)
                # for getting session variable:
                request.session['get_access'] = Token 
                request.session['get_username'] = username 
                request.session['get_role'] = user_role
                print(username)
                print(user_role)
                print('-=-=-=-=-=-=-==-')
                print(Token)
                if user_role == "SUPER_ADMIN":
                    messages.success(request,('Logged in successful'))
                    print('---------------------its SUPER_ADMIN---------------------')
                    return redirect('super_admin_func')
                elif user_role == "ADMIN":
                    messages.success(request,('Logged in successful'))
                    print('---------------------its ADMIN---------------------')
                    return redirect('admin_func')
                else:
                    messages.success(request,('Logged in successful'))
                    print('---------------------its USER---------------------')
                    return redirect('user_func')
            else:
                messages.error(request,("Wrong credentials. Try Again"))
                return render(request,'user/signin.html')
        return render(request,'user/signin.html')
    except:
        messages.error(request,'Wrong credentials or Admin not yet approved your Role')
        return redirect('user_signin')

def super_admin_func(request):
    try:
        get_token = request.session['get_access']
        header={'Authorization':'Bearer {toki}'.format(toki=get_token)}
        if request.POST.get('btnSaveRole','') == 'SaveOrder':
            print('-------------------------post role-------------')
            user =  request.POST['ddlUsername']
            role =  request.POST['ddlRole']
            data = {
                'user': user,
                'role': role,
                }
            response = requests.post('{url}manage_user/'.format(url=url),data=data,headers=header)
            print(response.text)
            get_response=response.json()
            print(get_response)
            if response.status_code > 300:
                get_token = request.session['get_access']
                header={'Authorization':'Bearer {toki}'.format(toki=get_token)}
                print('--------------------------response>300role----------------------------')
                messages.error(request,'Should select user and role')
                vehicle_type_data=requests.get('{url}create_vehicle_type/'.format(url=url),headers=header).json()
                user_data=requests.get('{url}create_user/'.format(url=url)).json()
                return render(request,'vehicle/super_admin.html',{'user_data':user_data,'vehicle_type_data':vehicle_type_data,'response':get_response})
            else:
                messages.success(request,("User role assigned successfully"))
                return redirect('super_admin_func')
        elif request.POST.get('btnSaveDetails','') == 'SaveDetails':
            print('-------------------------post role-------------')
            vehicle_number =  request.POST['txtVehicleNumber']
            vehicle_type =  request.POST['ddlVehicleType']
            vehicle_model =  request.POST['txtVehicleModel']
            vehicle_description =  request.POST['txtVehicleDescription']
            data = {
                'vehicle_number': vehicle_number,
                'vehicle_type_id': vehicle_type,
                'vehicle_model': vehicle_model,
                'vehicle_description': vehicle_description,
                }
            response = requests.post('{url}create_vehicle/'.format(url=url),data=data,headers=header)
            print(response.text)
            get_response=response.json()
            if response.status_code > 300:
                get_token = request.session['get_access']
                header={'Authorization':'Bearer {toki}'.format(toki=get_token)}
                print('--------------------------response>300vehicle----------------------------')
                messages.error(request,'All fields are mandatory to create vehicle details.')
                vehicle_type_data=requests.get('{url}create_vehicle_type/'.format(url=url),headers=header).json()
                user_data=requests.get('{url}create_user/'.format(url=url)).json()
                return render(request,'vehicle/super_admin.html',{'user_data':user_data,'vehicle_type_data':vehicle_type_data,'response':get_response})
            else:
                messages.success(request,("Vehicle details created successfully"))
                return redirect('super_admin_func')
        elif request.POST.get('btnSaveType','') == 'SaveType':
            print('-------------------------post type-------------')
            vehicle_type =  request.POST['txtType']
            data = {
                'vehicle_type': vehicle_type,
                }
            response = requests.post('{url}create_vehicle_type/'.format(url=url),data=data,headers=header)
            print(response.text)
            get_response=response.json()
            if response.status_code > 300:
                get_token = request.session['get_access']
                header={'Authorization':'Bearer {toki}'.format(toki=get_token)}
                print('--------------------------response>300type----------------------------')
                messages.error(request,'Vehicle type field empty.')
                vehicle_type_data=requests.get('{url}create_vehicle_type/'.format(url=url),headers=header).json()
                user_data=requests.get('{url}create_user/'.format(url=url)).json()
                return render(request,'vehicle/super_admin.html',{'user_data':user_data,'vehicle_type_data':vehicle_type_data,'response':get_response})
            else:
                messages.success(request,("Vehicle type created successfully"))
                return redirect('super_admin_func')
        else:
            get_token = request.session['get_access']
            header={'Authorization':'Bearer {toki}'.format(toki=get_token)}
            print('-------------------------else super admin-------------')
            # role_data=requests.get('{url}manage_user/'.format(url=url)).json()
            vehicle_type_data=requests.get('{url}create_vehicle_type/'.format(url=url),headers=header).json()
            user_data=requests.get('{url}create_user/'.format(url=url),headers=header).json()
            return render(request,'vehicle/super_admin.html',{'user_data':user_data,'vehicle_type_data':vehicle_type_data})
    except:
        return redirect('user_signin')


def admin_func(request):
    try:
        get_token = request.session['get_access']
        header={'Authorization':'Bearer {toki}'.format(toki=get_token)}
        response = requests.get('{url}list_vehicle/'.format(url=url),headers=header).json()
        vehicle_type_data=requests.get('{url}create_vehicle_type/'.format(url=url)).json()
        return render(request,'vehicle/list_vehicle.html',{'response' : response,'vehicle_type_data':vehicle_type_data})
    except:
        return redirect('user_signin')

def list_user_role(request):
    try:
        get_token = request.session['get_access']
        header={'Authorization':'Bearer {toki}'.format(toki=get_token)}
        role_data= requests.get('{url}user_role/'.format(url=url),headers=header).json()
        return render(request,'vehicle/user_role.html',{'role_data':role_data})
    except:
        return redirect('user_signin')

def list_vehicle_type(request):
    try:
        get_token = request.session['get_access']
        header={'Authorization':'Bearer {toki}'.format(toki=get_token)}
        vehicle_type_data = requests.get('{url}create_vehicle_type/'.format(url=url),headers=header).json()
        return render(request,'vehicle/vehicle_type_list.html',{'vehicle_type_data':vehicle_type_data})
    except:
        return redirect('user_signin')

def update_vehicle(request,id):
    try:
        get_token = request.session['get_access']
        header={'Authorization':'Bearer {toki}'.format(toki=get_token)}
        if request.method == 'POST':
            vehicle_number=request.POST['txtVehicleNumber']
            vehicle_type=request.POST['ddlVehicleType']
            vehicle_model=request.POST['txtVehicleModel']
            vehicle_description=request.POST['txtVehicleDescription']
            data={
                'vehicle_number':vehicle_number,
                'vehicle_type_id':vehicle_type,
                'vehicle_model':vehicle_model,
                'vehicle_description':vehicle_description,
                }
            response=requests.put('{url}manage_vehicle/{pk}/'.format(url=url, pk=id), data=data)
            print('-------update vehicle-------')
            print(response.text)
            get_response = response.json()
            if response.status_code > 300:
                print('--------------------------response>300vehicle----------------------------')
                messages.error(request,'Failed to update')
                return redirect('admin_func')
            else:
                messages.success(request,("Vehicle data updated successfully"))
                return redirect('admin_func')
        else:
            print('-------------------------else update vehicle-------------')
            return redirect('admin_func')
    except:
        return redirect('user_signin')

def update_user_role(request,id):
    try:
        get_token = request.session['get_access']
        header={'Authorization':'Bearer {toki}'.format(toki=get_token)}
        if request.method == 'POST':
            user=request.POST['ddlUser']
            role=request.POST['ddlRole']
            data={
                'user':user,
                'role':role,
                }
            response=requests.put('{url}manage_user/{pk}/'.format(url=url, pk=id), data=data,headers=header)
            print('-------update role-------')
            print(response.text)
            get_response = response.json()
            if response.status_code > 300:
                print('--------------------------response>300 role----------------------------')
                messages.error(request,'Failed to update')
                return redirect('list_user_role')
            else:
                messages.success(request,("User Role updated successfully"))
                return redirect('list_user_role')
        else:
            print('-------------------------else update role-------------')
            return redirect('list_user_role')
    except:
        return redirect('user_signin')

def update_type(request,id):
    try:
        get_token = request.session['get_access']
        header={'Authorization':'Bearer {toki}'.format(toki=get_token)}
        if request.method == 'POST':
            vehicle_type=request.POST['txtVehicleType']
            data={
                'vehicle_type':vehicle_type,
                }
            response=requests.put('{url}manage_vehicle_type/{pk}/'.format(url=url, pk=id), data=data,headers=header)
            print('-------update type-------')
            print(response.text)
            get_response = response.json()
            if response.status_code > 300:
                print('--------------------------response>300 type----------------------------')
                messages.error(request,'Failed to update')
                return redirect('list_vehicle_type')
            else:
                messages.success(request,("Vehicle type updated successfully"))
                return redirect('list_vehicle_type')
        else:
            print('-------------------------else update type-------------')
            return redirect('list_vehicle_type')
    except:
        return redirect('user_signin')

def user_func(request):
    try:
        get_token = request.session['get_access']
        header={'Authorization':'Bearer {toki}'.format(toki=get_token)}
        vehicle_data = requests.get('{url}list_vehicle/'.format(url=url),headers=header).json()
        print(vehicle_data)
        return render(request,'vehicle/view_vehicle.html',{'vehicle_data_list' : vehicle_data})
    except:
        return redirect('user_signin')


def delete_user_role(request,id):
    try:
        get_token = request.session['get_access']
        header={'Authorization':'Bearer {toki}'.format(toki=get_token)}
        response=requests.delete('{url}manage_user/{pk}/'.format(url=url, pk=id))
        messages.success(request,("Role for user deleted successfully"))
        return redirect('list_user_role')
    except:
        return redirect('user_signin')

def delete_vehicle(request,id):
    try:
        get_token = request.session['get_access']
        header={'Authorization':'Bearer {toki}'.format(toki=get_token)}
        response=requests.delete('{url}manage_vehicle/{pk}/'.format(url=url, pk=id),headers=header)
        messages.success(request,("Vehicle details deleted successfully"))
        return redirect('admin_func')
    except:
        return redirect('user_signin')


def delete_type(request,id):
    try:
        get_token = request.session['get_access']
        header={'Authorization':'Bearer {toki}'.format(toki=get_token)}
        response=requests.delete('{url}manage_vehicle_type/{pk}/'.format(url=url, pk=id))
        messages.success(request,("Vehicle type deleted successfully"))
        return redirect('list_vehicle_type')
    except:
        return redirect('user_signin')

def user_logout(request):
    get_token = request.session['get_access']
    header={"Content-Type":"application/json; charset=UTF-8", 'Authorization':'Token {toki}'.format(toki=get_token)}
    logout_reponse = requests.post('{url}logout/'.format(url=url), headers=header)
    print(logout_reponse)
    logout(request)
    messages.success(request,("You were logged out"))
    return redirect(user_signin)

