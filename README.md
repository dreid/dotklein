# dotklein

dotklein is an example configuration for running a simple klein "Hello, world!"
app on dotcloud.

## How does it work?

It's actually pretty simple.  It uses the standard python service type and
simply replaces the uwsgi nginx configuration with a proxy_pass directive to
talk to a process managed by supervisord.
