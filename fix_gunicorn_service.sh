#!/bin/bash

# Fix Gunicorn Service to use run.py instead of app.py

echo "🔧 Fixing Gunicorn service configuration..."

# Stop the service
systemctl stop erp 2>/dev/null

# Create correct Gunicorn service
cat > /etc/systemd/system/erp.service << 'EOF'
[Unit]
Description=ERP Flask Application
After=network.target

[Service]
User=root
Group=www-data
WorkingDirectory=/root/DED
Environment="PATH=/root/DED/venv/bin"
ExecStart=/root/DED/venv/bin/gunicorn --workers 3 --bind 0.0.0.0:8000 run:app

[Install]
WantedBy=multi-user.target
EOF

# Reload systemd
systemctl daemon-reload

# Start and enable service
systemctl start erp
systemctl enable erp

# Check status
echo ""
echo "✅ Service configuration updated!"
echo ""
echo "Checking service status..."
systemctl status erp --no-pager

echo ""
echo "🎉 Done! Your application should now be running on port 8000"

