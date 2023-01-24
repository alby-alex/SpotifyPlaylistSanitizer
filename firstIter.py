import tekore as tk

client_id = '028a0cf47362411fb1eeb6c9ace76ad9'
client_secret = 'f734389c17094d4c99f7e7383bfb741e'

redirect_uri = "https://example.com/callback"
user_token = tk.prompt_for_user_token(
    client_id,
    client_secret,
    redirect_uri,
    scope=tk.scope.every
)
conf = (client_id, client_secret, redirect_uri, user_token.refresh_token)
tk.config_to_file('tekore.cfg', conf)


