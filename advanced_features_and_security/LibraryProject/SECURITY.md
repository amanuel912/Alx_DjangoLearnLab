# Security Measures Implemented

1. HTTPS enforced with SECURE_SSL_REDIRECT.
2. HSTS enabled for 1 year with all subdomains.
3. Cookies are marked secure for HTTPS only.
4. Clickjacking and XSS protection via X_FRAME_OPTIONS, SECURE_CONTENT_TYPE_NOSNIFF, SECURE_BROWSER_XSS_FILTER.
5. Deployment must include valid SSL/TLS certificates and proper web server configuration.
