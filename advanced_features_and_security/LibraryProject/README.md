# Managing Permissions and Groups in Django

This project demonstrates role-based access control using Django groups and custom permissions.

## Custom Permissions

Custom permissions were added to the Book model:

- can_view
- can_create
- can_edit
- can_delete

## Groups

Three groups were created:

### Viewers
- can_view

### Editors
- can_view
- can_create
- can_edit

### Admins
- can_view
- can_create
- can_edit
- can_delete

## Views Protection

Views are protected using Django's permission_required decorator.

Examples:

@permission_required('relationship_app.can_view', raise_exception=True)

@permission_required('relationship_app.can_create', raise_exception=True)

@permission_required('relationship_app.can_edit', raise_exception=True)

@permission_required('relationship_app.can_delete', raise_exception=True)

## Testing

Test users were created and assigned to groups to verify access control:

- Viewer: can only view books
- Editor: can view, create, and edit books
- Admin: full access including delete

## Security Practices

- DEBUG disabled
- CSRF protection enabled using {% csrf_token %}
- Secure cookies enabled
- XSS, clickjacking, and MIME sniffing protections enabled
- Django ORM used to prevent SQL injection
- Basic Content Security Policy applied


## HTTPS and Secure Redirects

The application is configured to enforce HTTPS using Django security settings.

Implemented settings:

- SECURE_SSL_REDIRECT = True (redirects all HTTP traffic to HTTPS)
- SECURE_HSTS_SECONDS = 31536000
- SECURE_HSTS_INCLUDE_SUBDOMAINS = True
- SECURE_HSTS_PRELOAD = True

Secure cookies:

- SESSION_COOKIE_SECURE = True
- CSRF_COOKIE_SECURE = True

Security headers:

- X_FRAME_OPTIONS = "DENY"
- SECURE_CONTENT_TYPE_NOSNIFF = True
- SECURE_BROWSER_XSS_FILTER = True

### Deployment Notes

In production, HTTPS should be enabled using SSL/TLS certificates configured at the web server level (e.g., Nginx or Apache). Certificates can be provided by services such as Let's Encrypt.

All HTTP traffic is redirected to HTTPS by Django using SECURE_SSL_REDIRECT.

## Security Review

These settings protect against:

- Man-in-the-middle attacks (HTTPS + HSTS)
- Clickjacking (X_FRAME_OPTIONS)
- XSS attacks (SECURE_BROWSER_XSS_FILTER)
- MIME sniffing (SECURE_CONTENT_TYPE_NOSNIFF)
- Cookie hijacking (secure cookies)

Further improvements may include using django-csp and regular security audits.
