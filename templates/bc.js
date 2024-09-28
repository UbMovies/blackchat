
        function convertToLowercase() {
        let senderInput = document.getElementById('senderInput');
        senderInput.value = senderInput.value.toLowerCase();
    }
        const socket = io.connect('http://' + document.domain + ':' + location.port);

        
        const key = '1100c1011145e4f';  
        
        function encryptMessage(message, sender) {
            
        
            const messageWithSender = `${sender}:${message}`;
            return CryptoJS.AES.encrypt(messageWithSender, key).toString();
        }

        
        function decryptMessage(encryptedMessage) {
            const bytes = CryptoJS.AES.decrypt(encryptedMessage, key);
            return bytes.toString(CryptoJS.enc.Utf8);
        }

        
        socket.on('message', function(data) {
            const decryptedMessage = decryptMessage(data.message);
            const [sender, message] = decryptedMessage.split(':');

            const messageDiv = document.createElement('div');
            messageDiv.classList.add('message');
            
            const senderDiv = document.createElement('div');
            senderDiv.classList.add('sender');
            senderDiv.textContent = sender + ':';
            
            const messageContentDiv = document.createElement('div');
            messageContentDiv.textContent = message;
            
            messageDiv.appendChild(senderDiv);
            messageDiv.appendChild(messageContentDiv);
            
            document.getElementById('messages').appendChild(messageDiv);
        });

        
        function sendMessage() {
            const message = document.getElementById('messageInput').value;
            const sender = document.getElementById('senderInput').value || 'Anonymous';
            
            
            const encryptedMessage = encryptMessage(message, sender);
            socket.send({ message: encryptedMessage, sender });
            document.getElementById('messageInput').value = '';
        }
    