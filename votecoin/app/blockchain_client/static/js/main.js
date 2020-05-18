$(document).ready(function() {
    $(document).on('click', '#generate-wallet', function() {
        $.ajax({
            url: '/wallet/new',
            type: 'GET',
            success: function(response) {
                document.getElementById('public_key').innerHTML = response['public_key'];
                document.getElementById('private_key').innerHTML = response['private_key'];
                document.getElementById('warning').style.display = 'block';
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});