## Networking Basics


Host: any device that can send or recieve information
    Client: a host that is sending a requist to a server
    Server: a host that is responding to requists
ex: computers, printers, recievers, mobile phones, ....

IP Adress: the identifier of the host in a network
ex: starting from 0.0.0.0 to 255.255.255.255 and this is the IPv4

Network: A way of grouping connecting more than one host to each other
Networks are the automation of transfering ifnormations physically using CDs and USBs
ex: connecting two computers or a computer and a mobile using a wire or wirelessly


### Network Components
if we have a very very long cable to transfere information between two hosts, the signal will be weaker and weaker unilt it dissappears, so something called a **Repeater** is used to repeat the signal to make it stronger again.

some way of connecting more than a host to each other is to connect every one with every one, but that is not scalable when the network needs to get bigger and bigger, to solve that we can use a **Hub** and connect every host to is, hosts will send informations to the **Hub** and it will repeat the signal to each host connected to it.
that seems unsecure and resource consuming, imagine a network of 10 hosts and host number 4 wants to send an information to host number 8 that means not only host number 8 will get that information, but all the 10 hosts will get it, and that takes us to the next component.
**Bridges**: is a way of connecting two hubs (aka two networks) with each others, informations will not pass the other side of the bridge unless it is going to a host that is residing in the other side of the pridge, otherwise the bridge will not repeat the signal coming to it.
but **Bridges** did not replaced **Hubs** and still the information will be with every one on the other side of the bridge if it just passed the bridge, **Hubs** redirect signals to every one and **Bridges** knows if it is necessary for the information to go to the other side (it knows which hub is sending the information -letter- and which is receiving it)
so if it is possible to compine these components to make sure that the signal stay strong across the line and goes just for the reciever we want, and that is what **switches** does: it facilitates the transportation of informations within a network.

now we have a network and our neighbours have a network and the school we have in our city have a network, each network have a **switch** managing transportation inside that network, what if we need to connect all these 3 networks together? should we throw away 2 switces and buy more wires to connect every one to the same switch? of course not. what if another neighbour made a network and what if the supermarked decided to make a network, will it be suffecient to connect them in that way? it would be better if we managed to connect these network with each other instead, and make a network of networks!
**Routers** does the job of connecting networks -switches- with each other, and it facilitates that connection adding security, filtering, and redirecting, which **switches** does not offer because it facilitates the connection in an inclosed network so security is not an issue here, for example connicteng all the computers in a lab will be ok if we did it with just a switch. no hacker will try to steal information from you in the same room, he can just steal the whole computer 😂
**Routers** knows which networks they are attached to, and that information is stored in a *Routing Table*, *Routing* is simply redirecting something in the correct route, for example this article you are reading is an information someday I pushed it to Github, this information have gone across the **internet** network which consists of tons of **Routes** and **Routers** that redirectes informations to the correct route-aka next joint or router to redirect it to the next one and so on- until it reaches its palce in the Github server, some other day you requisted that information from Github and this article have traveled another route to get to you with the help of **Routers**.

source: [https://www.youtube.com/playlist?list=PLIFyRwBY_4bRLmKfP1KnZA6rZbRHtxmXi]

### OSI Model
so remember what networks do? what if there is nothing called **internet** -International Network- and I wanted to send you an information? I would have to save that information into a USB or CD and travel to send it to you, or I might ship it to you using any shipping service. Oh no how I would send an infromation to the shipping service that I need to send you an infromation. and if any of that gone wrong, how much time would it take to just know that something went wrong.

