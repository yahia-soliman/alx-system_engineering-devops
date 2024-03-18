## The URL
Lets have a look to that string you have written in your browser `google.com`,
this is called a domain name, it consists of a top-level domain TLD and a second-level domain,
you can add another part, the sub-domain, for example: `www.google.com`, "www" is the sub-domain.

### So why that domain name thing is important?
Imagine some one told you to send a message to Mrs Mona, who is Mrs Mona, and where she is right now?
you might know the address of Mrs Mona, and you might ask someone, this is the same situation for your browser,
your browser must know the address of Mr `google.com` to be albe to comunicate with it, the address of a website is the
IP address of its hosting server, for example `142.251.209.4` is the IP address of a the one hosting `google.com`,
your browser resolves the `google.com` (the company name that you know) to `142.251.209.4` (the digital Internet Protocol Address that machines understand),
but how did it knew the IP address, thats because of the Domain Name System

## The DNS, Domain Name System
Let us get back to Mrs Mona, the first thing you would think of is, (do I know where is Mrs Mona? hava I visited her before?),
for your browser the first place it looks into for Mr `google.com` is its cached domain names, if it does not know Mr `google.com`,
it will ask your operating system if it knows the IP address of Mr `google.com`, if the OS does not know, then a DNS query is send
to a DNS resolver, and if the resolver also does not know it, it well ask the Root name server (and any domain name resolver must be knowing the IP address of the Root name server)
the Root name server well tell the resolver where to find the ".com" domains, and it will point the resolver to the ".com" TLD name server,
now the TLD name server well point the resolver to the authoritative name server that is the last hope to know the IP address of Mr `google.com`,
if it does not know, then `google.com` is not a registered domain name, but luckily the resolver have known that `142.251.209.4` is the IP address of `google.com`,
it gives it to your Operating System, then the OS passes it to your browser, the browser saves it in cache to remember it for later, and finally your browser knows
the IP address of `google.com`, but how would your borowser communicate with it? and what language does Mr `google.com` speak?

## The TCP IP
The P stands for protocol, and it is a set of rules that members of a network must follow to communicate successfully, in our story here, the network is the internet,
and the members of that networks are computers, servers, routers, firewalls, etc..
First each one of those members must have a unique address this, in the Internet Protocol it is the IP address.
Second, the members must specify the way they will send messages to each other, in the Transmission Control Protocol, when a member send a message to another,
the one how got a message replies back with the same message to confirm that is has recieved the message, and after that it might respond or not,
luckily Mr `google.com` responded and gave us a white page with google's logo and a search bar, how did it generated that response.

## The Server
For a website like `google.com` which have tons of visits in each minute, there must be load balancers, to distribute that high load, and to mitigate the single point of failure,
Mr `google.com`'s load balancer distributed our request to one of the application servers, the application server that was responsible for respoding to our request,
communicates with it's corresponding database server, to get the resent photo of google's logo depending on any seasonal change,
after finishing it's logic the application server replies to the load balancer and the load balancer replies to our browser,
our boweser then renders the photo and the search bar for us depending on the HTML structure send from the server.
