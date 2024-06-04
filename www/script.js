fetch('checkConnection.php')
    .then(response => response.text())
    .then(result => {
        const connectionStatusElement = document.getElementById('connectionStatus');
        if (result === 'true') {
            connectionStatusElement.textContent = 'Connecté au serveur Azure SQL Flexible Server';
        } else {
            connectionStatusElement.textContent = 'Échec de la connexion au serveur Azure SQL Flexible Server';
        }
    });
