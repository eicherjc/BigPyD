# BigPyD - Pythonic framework for working with BigID

Note: this is still very much a work in progress, so more functionality to follow.

This framework allows you to easily in a pythonic way get a valid session with BigID and then both access data programatically as well as kick off some actions inside of BigID.

### GetSession

This module allows you to create your session with BigID.

It contains two methods. One being the `getSession()` method which does not enforce secure SSL connections, and the `getSessionSSL()` method which will enforce SSL unless you specificy otherwise.

`getSession()` requires three parameters: the URL to the BigID application server, the username, and the password.

> getSession(url, user, password)

For example:

> MyBigIDSession = getSession('https://mybigidserver.com','my_username','my_password')

This will return a `requests` library session object that's been updated to include a new header with the authorization token to make new requests to the BigID application server. This also adds a new attribute `MyBigIDSession.url` which will save the url you provided to easily access for future requests.

You could at this point simply use this session to make new calls against the BigID application server without passing this session to any of the other modules or methods in this package.

For example:

> r = MyBigIDSession.get(url=MyBigIDSession.url + "/api/v1/data-catalog/?format=json", headers=MyBigIDSession.headers, verify=False)
> r.json()

This code would return the full listing of your catalog.

The `getSessionSSL()` method works the same exact way, it just enforces SSL unless you specify `ssl=False` as the last parameter.

> getSessionSSL(url, user, passowrd, ssl=True)

### DSAR

This module allows you to search entities, run DSAR, view profiles, and run a deletion validation.

These methods are `DSAR.search()`, `DSAR.run()`, `DSAR.profiles()`, and `DSAR.delete()`.


When you pass a `getSession` object to the DSAR class, it will create a DSAR object that contains your BigID session and will automatically pull the default search profile and allow you to start making DSAR app requests.

> MyDSARObject = DSAR(MyBigIDSession)


The `DSAR.search()` method requires a user name or a user id, and optionally you can specify `allAttributes="false"` (default is `allAttributes="true"`).

> DSAR.search(userName="", userId="", allAttributes="true")

For example you could run a search for an entity "Karen George" simply using the code below:

> MyDSARObject.search('Karen George')


The `DSAR.run()` method requires a user id, display name (name that the request will be identified as), and optionally you can add a python dictionary of additional search attributes.

> DSAR.run(userId, displayName, attributes={})

You could run a DSAR like this:

> MyDSARObject.run('<entitys-unique-id>','Karen George',{email : karen.george@domainname.com, country: USA})


The `DSAR.profiles()` method simply returns a json document of all the profiles available in BigID. There are no paremeters.

> MyDSARObject.profiles()

This method is useful if you want to see the other available profiles and then update the `MyDSARObject.profileId` attribute to be something other than the default for use with the other methods in this module.


The `DSAR.delete()` method requires a requestId of a previously completed DSAR.

> DSAR.delete('<requestId>')

You could run a deletion valdation like this:

> MyDSARObject.delete('<requestId')

