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

