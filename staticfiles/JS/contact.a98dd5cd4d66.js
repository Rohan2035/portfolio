function sendMail() {

    document.getElementById('alert-danger').hidden=true;
    document.getElementById('alert-success').hidden=true;


    var params = {

        sender_name: document.getElementById('name').value,
        from_name: document.getElementById('email').value,
        message: document.getElementById('message').value,

    };

    if(document.getElementById('name').value == "" || document.getElementById('email').value == "" || document.getElementById('message').value == "") {

        document.getElementById('alert-danger').hidden=false;

    }

    else {

        emailjs.send('service_b7iq8fm', 'template_kc1v6sb', params)
            .then(function(response) {
                
                document.getElementById('alert-success').hidden=false;


            }, function(error) {
                
                document.getElementById('alert-danger').hidden=false;

            });

        document.getElementById('name').value = "";
        document.getElementById('email').value = "";
        document.getElementById('message').value = "";

    }
    
    return false;

}