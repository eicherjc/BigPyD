# BigPyD - Pythonic framework for working with BigID

Note: this is still very much a work in progress, so more functionality to follow.

This framework allows you to easily in a pythonic way get a valid session with BigID and then both access data programatically as well as kick off some actions inside of BigID.

### GetSession

This module allows you to create your session with BigID. It contains just one method, being the `getSession()` method.

`BigPyD.getSession()` requires three parameters: the URL to the BigID application server, the username, and the password. The ssl parameter is optional and defaults to false.

> getSession(url, user, password, ssl=False)

For example:

> MyBigIDSession = BigPyD.getSession('https://mybigidserver.com','my_username','my_password')

This will return a `requests` session object that's been updated to include a new header with the authorization token to make new requests to the BigID application server. This also adds a new attribute `MyBigIDSession.url` which will save the url you provided to easily access for future requests.

You could at this point simply use this session to make new calls against the BigID application server without passing this session to any of the other modules or methods in this package.

For example:

> r = MyBigIDSession.get(url=MyBigIDSession.url + "/api/v1/data-catalog/?format=json")
> r.json()

This code would return the full listing of your catalog.


### DSAR

This module allows you to search entities, run DSAR, run bulk DSAR, view scans, view scan details, run deletion validation, view profiles.

When you pass a `BigPyD.getSession` object to the DSAR class, it will create a DSAR object that contains your BigID session and will automatically pull the default search profile and allow you to start making DSAR app requests.

> MyDSARObject = BigPyD.DSAR(MyBigIDSession)

For example you could run a search for an entity "Karen George" simply using the code below:

> MyDSARObject.search('Karen George')


### Scan

This module allows you to run scans, view scans, stop scans, and view profiles.

When you pass a `BigPyD.getSession` object to the Scan class, it will create a Scan object that contains your BigID session and will automatically pull the default scan profile and allow you to start running scans.

> MyScanObject = BigPyD.Scan(MyBigIDSession)

For example you could run a scan with the default profile simply using the code below:

> MyScanObject.run()

Or specify a specific scan profile:

> MyScanObject.run('Oracle Full DS Scan')


### Policy

This module allows you to export a csv of all your polices and set a new policy.

When you pass a `BigPyD.getSession` object to the Policy class, it will create a Policy object that contains your BigID session.

> MyPolicyObject = BigPyD.Policy(MyBigIDSession)

For example you could set a new policy using the below code:

> MyPolicyObject.setPolicy(Data)

Where the `Data` object is a python dictionary that contains all the policy definition JSON data.