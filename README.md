# RPC-scheduler

### This repository is used for my MEng Individual Project at Imperial College London

## Introduction
Tail latency is vital for vendors that want to provide guarantees to their clients, which is particularly hard to control when dealing with RPCs (remote procedure calls) at the µs scale. Current solutions utilize streaming or datagram-based transport protocols for RPCs that impose overheads and limit the design flexibility, which is where innovations such as R2P2[1] build on top of UDP to overcome this. However, custom or UDP-based protocols are currently not enough to convince industry partners to move away from a more secure and well-known TCP solution. 

My project aims to convince industry to adopt more sophisticated ways of using or building on top of TCP so that we can reap similar benefits shown in R2P2[1] while not sacrificing secuirty. It has been previously shown that TCP-based solution can be used, specifically in object storage[2], to reduce the overhead in the typical frontend proxy architecture deployed in industry.  

## Background
### Issues with Frontend Proxy Architecture
Industry typically uses a frontend proxy architecture to handle the routing of RPCs within their service mesh. Usually, this is done using NGINX as a frontend server that recieves the request from a client and forwards it to at least one of the backend servers. In this architecture, the frontend server compute resources are being fully utilised, while the backend servers are under-utilising. As a result, this design suffers in terms of throughput. 

### Issues with Application-Aware Architectures

## Project Plan

## Evaluation Plan

## Ethical Issues

## References
1. https://www.usenix.org/system/files/atc19-kogias-r2p2_0.pdf
2. https://micchie.net/files/prism-nsdi21.pdf
