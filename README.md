# Secure Chat Web Appliction | chatnet.lk

**Authors:**
  - IT21292040 | Sasanka M.W.K.L
  - IT21292736 | Ayeshani K.M.N

**Overview**

  - ChatNet is a secure web-based chat application developed by SLIIT BSc (Hons) IT students specializing in Cyber Security, as part of the Secure Software System (IE3042) module. This application enables real-time communication between users and emphasizes advanced security features to ensure data protection.

![Diagram](/assets/images/logo.png "LOGO DESIGN")


Welcome to the official GitHub repository for chatnet.lk, an innovative web-based chat platform that aims to provide seamless and secure communication solutions. This project is designed to cater to users looking for reliable online chat services with an emphasis on privacy and user-friendliness.

**Features**
  - End-to-End Encryption: Ensures that messages are only readable by the sender and the intended recipients.
  - User Authentication: Robust authentication system to verify user identities and manage sessions securely.
  - Password Hashing: Utilizes strong hashing algorithms to securely store user passwords.
  - Spam Detection: Integrates a machine learning model to identify and filter out spam messages.
  - Real-Time Communication: Allows users to exchange messages instantly without needing to refresh their browsers.
  - User Blocking: Users can block other users, enhancing control over personal interaction spaces.
  - Secure Session Management: Sessions are managed securely to prevent unauthorized access.
  - Logging: Detailed logs for security monitoring and auditing purposes.

**Technologies**
  - Frontend: HTML, CSS, JavaScript, jQuery
  - Backend: PHP, CodeIgniter Framework
  - Database: MySQL
  - Security: AES for encryption, PBKDF2 for password hashing

**Prerequisites**
  Before installing the ChatNet application, ensure you have the following installed:

  -  PHP 7.4 or higher
  -  MySQL 5.7 or higher
  - Apache 2.4 or higher (with mod_rewrite enabled)
  -  Composer (for managing PHP dependencies)


**Installation**

# Clone the repository:
    git clone https://github.com/Lakiya7/chatnet.lk.git

# Navigate to the project directory:
    cd chatnet

# Set up the Database:

  Create a new MySQL database named chatigniter
  Export the chatigniter.sql located in db Folder
  mysql -u username -p chatnetdb < path/to/chatigniter.sql

# Configure the Application

  Navigate to the app/config directory.
  Copy the config.sample.php to config.php and edit it to set your database credentials and other environment-specific configurations.

# Configure Apache

  Set up an Apache virtual host to point to the public directory of the cloned repository.
  Ensure that mod_rewrite is enabled for pretty URLs.

  nano /etc/httpd/conf.d/site1.conf
 
  ```
<VirtualHost *:80>
      ServerName Chatnet.lk
      DocumentRoot /var/www/html/Chat_Net
      <Directory "/var/www/html/Chat_Net">
          Require all granted
      </Directory>
  </VirtualHost>
```
# Adjust Permissions
```
  chmod -R 775 /path/to/chat_net/upload
```
# Running the Application

  After installation, start your Apache server and visit the application through the configured domain, e.g., **http://127.0.0.1**. You should be able to register a new user account and start chatting immediately.


------------------------------------------------------------------------------------------------


**Secure Coding Practices**
To maintain the integrity and security of the application, we adhere to best practices in secure coding:
  - Input Validation: All inputs are validated on the server-side to prevent SQL injection and XSS attacks.
  - Session Security: Use of secure session cookies and regeneration of session IDs to prevent session hijacking.
  -	Access Controls: Implementation of role-based access controls to ensure users can only access appropriate features.
  -	Encryption: Utilization of AES for message encryption and secure transmission protocols to protect data in transit.


**Contributing**
Contributions to the ChatNet project are welcome! Please fork the repository, make your changes, and submit a pull request to the main branch. For major changes, please open an issue first to discuss what you would like to change.


© 2024 Chat Net Web. All rights reserved.




