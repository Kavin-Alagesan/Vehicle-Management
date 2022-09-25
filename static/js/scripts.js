$(document).ready(function () {
    $(".alert").hide(5000);
});

function validateFormRegister() {
    let val_name = document.forms["formRegister"]["txtUsername"].value;
    if (val_name == "") {
        alert("Username should not be empty");
        return false;
    }
    let val_email = document.forms["formRegister"]["txtEmail"].value;
    if (val_email == "") {
        alert("Email should not be empty");
        return false;
    }
	let val_password = document.forms["formRegister"]["txtPwd1"].value;
    if (val_password == "") {
        alert("Password should not be empty");
        return false;
    }
	let val_password2 = document.forms["formRegister"]["txtpwd2"].value;
    if (val_password2 == "") {
        alert("Confirm password should not be empty");
        return false;
    }
}

function validateFormLogin() {
    let val_name = document.forms["formLogin"]["txtUsername"].value;
    if (val_name == "") {
        alert("Username should not be empty");
        return false;
    }
	let val_password = document.forms["formLogin"]["txtPwd"].value;
    if (val_password == "") {
        alert("Password should not be empty");
        return false;
    }
}

function validateFormRole() {
    let val_name = document.forms["formCreateRole"]["ddlUsername"].value;
    if (val_name == "0") {
        alert("Username should select");
        return false;
    }
	let val_role = document.forms["formCreateRole"]["ddlRole"].value;
    if (val_role == "0") {
        alert("Role should select");
        return false;
    }
}

function validateFormVehicle() {
    let val_number = document.forms["formCreateVehicle"]["txtVehicleNumber"].value;
    if (val_number == "") {
        alert("Vehicle number should not be empty");
        return false;
    }
	let val_type = document.forms["formCreateVehicle"]["ddlVehicleType"].value;
    if (val_type == "0") {
        alert("Vehicle type should select");
        return false;
    }
    let val_model = document.forms["formCreateVehicle"]["txtVehicleModel"].value;
    if (val_model == "") {
        alert("Vehicle model should not be empty");
        return false;
    }
    let val_description = document.forms["formCreateVehicle"]["txtVehicleDescription"].value;
    if (val_description == "") {
        alert("Description should not be empty");
        return false;
    }
}

function validateFormType() {
    let val_type = document.forms["formCreateType"]["txtType"].value;
    if (val_type == "") {
        alert("Vehicle type field empty");
        return false;
    }
}

