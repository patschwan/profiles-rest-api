from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""
    # permission class defined by has_object_permission
    # das wird jedes mal, wenn Aufruf erfolgt geprüft

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            # if it is e.g. GET or POST (=SAFE methods)
            return True

        # entspricht die Object ID der angemeldeten UserID
        return obj.id == request.user.id # returns a boolean
