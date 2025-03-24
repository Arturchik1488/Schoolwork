// Script to auto-dismiss flash messages after 5 seconds
document.addEventListener('DOMContentLoaded', function() {
    const alerts = document.querySelectorAll('.alert:not(.alert-persistent)');
    
    alerts.forEach(alert => {
        setTimeout(() => {
            // Use Bootstrap's alert dismissal method
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });
});
