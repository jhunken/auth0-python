from .base import AuthenticationBase
import warnings


class Users(AuthenticationBase):

    """Userinfo related endpoints.

    Args:
        domain (str): Your auth0 domain (e.g: username.auth0.com)
    """

    def userinfo(self, access_token):

        """Returns the user information based on the Auth0 access token.
        This endpoint will work only if openid was granted as a scope for the access_token.

        Args:
            access_token (str): Auth0 access token (obtained during login).

        Returns:
            The user profile.
        """

        return self.get(
            url='https://{}/userinfo'.format(self.domain),
            headers={'Authorization': 'Bearer {}'.format(access_token)}
        )

    def tokeninfo(self, jwt):

        """Returns user profile based on the user's jwt

        Validates a JSON Web Token (signature and expiration) and returns the
        user information associated with the user id (sub property) of
        the token.

        Args:
            jwt (str): User's jwt

        Returns:
            The user profile.
        """
        warnings.warn("/tokeninfo will be deprecated in future releases", DeprecationWarning)
        return self.post(
            url='https://{}/tokeninfo'.format(self.domain),
            data={'id_token': jwt},
            headers={'Content-Type': 'application/json'}
        )
