# dbxs
A library to allow tcp socket-like communication over Dropbox

## How it works
you initialise a dbx instance like so

	dbx = dbxs.Dropbox(api_key)

the server then starts a listener like so

	server = dbx.Server(connection_id)

with `connection_id` being a unique identifier for each socket (think of it like a port). the client then connects like so

	client = dbx.Client(connection_id)

and communication ensues with `.send/.recv`

there are also quick functions that have been named for ease

	socket = dbx.socket()
	conn, addr = socket.accept()

	client = dbx.socket()
	client.connect(connection_id)

as you may have noticed, the server can accept any connection