
$(document).ready(function() {
    // Assuming you have a button with id 'send_message' to send messages
    $('#send_message').click(function(e) {
        e.preventDefault();
        var message = $('#messageText').val(); // Get the message from input box

        // Check if the message is spam
        $.ajax({
            url: 'http://192.168.60.8:5000/predict',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ message: message }),
            success: function(response) {
                if (response.is_spam) {
                    alert('Spam detected: ' + message);
                } else {
                    // Append message to chat if not spam
                    $('#chat_message_area').append('<div>' + message + '</div>');
                }
                $('#messageText').val(''); // Clear the message input box
            },
            error: function(error) {
                console.error('Error detecting spam:', error);
            }
        });
    });
});