# RPC-scheduler

### This repository is used for my MEng Individual Project at Imperial College London

## Introduction
Tail latency is vital for vendors that want to provide guarantees to their clients, which is particularly hard to control when dealing with RPCs (remote procedure calls) at the µs scale. Current solutions utilize streaming or datagram-based transport protocols for RPCs that impose overheads and limit the design flexibility, which is where innovations such as R2P2[1] build on top of UDP to overcome this. However, custom/UDP-based protocols are currently not enough to convince industry partners to move away from a more secure and well-known TCP solution. 

My project aims to convince industry to adopt more sophisticated ways of using or building on top of TCP so that we can reap similar benefits shown in R2P2[1] while not sacrificing security. It has been previously shown that a TCP-based solution can be used, specifically in object storage [2], to reduce the overhead in the typical frontend proxy architecture deployed in industry.  

## Background
### Queueing Theory
#### Causes for Imbalance in Queues [3]:
1. Persistent imbalance occurs when different queues observe different packet arrival rates over long intervals. This occurs when there is a connection or data skew.
2. Temporary queueing caused from arrival bursts (even when the system is not saturated). Even if the time to process each request is fixed, the 'bursts' which caused the temporary imbalance of queus leads to a gradual increase in tail latency.
3. Backlog and head-of-line blocking caused due to service time variability. Long requests can occupy processor for a long time, thus leading to a backlog of pending requests which causes a sever increase in tail latency as a result. 

#### Types of FCFS Queue Models [3]:
- Centralised-FCFS: all workers process events from a single (centralised) queue.
- Partitioned-FCFS: each worker have their own private work queue which they process from.

We note that single-queue multi-worker models perform better than distributed multi-queue models. This is due to systems with multiple queues are prone to temporary load imbalance, which can create a backlog on some worker queues while others are empty.
We also should note that FCFS allocation performs better in regards to tail latency for distributions with low dispersion [70 Zygos Paper, 3]. 


### Current Architectures
#### Issues with Frontend Proxy Architecture [2]:
Industry typically uses a frontend proxy architecture to handle the routing of RPCs within their service mesh. Usually, this is done using NGINX as a frontend server that recieves the request from a client and forwards it to at least one of the backend servers. In this architecture, the frontend server compute resources are being fully utilised, while the backend servers' resources are under-utilised. As a result, this design suffers in terms of throughput. 

#### Issues with Application-Aware Architectures [2]:
Recent progress have introduced the use of content-based routing architectures where the backend servers interact with programmable switches. This results in an improvement in throughput, latency, and resilience to skew (which is prevalent in realistic workloads), due to the switch's ability to redirect traffic that would otherwise be arriving at congested backend nodes. 

Although this is promising, the biggest issue it faces is that these solutions are UDP-based. This restricts clients to using a custom UDP-based protocol where they would implement loss recovery and congestion control functionality themselves, which is a non-trivial task. In addition, since it does not fuly support TCP it lacks support for industry standrd TLS security or popular application-level protocols. As a result, despite it's great progress in the academic field, industry is not as keen to adopt it yet. 

## Project Plan

## Evaluation Plan

## Ethical Issues

## References
1. https://www.usenix.org/system/files/atc19-kogias-r2p2_0.pdf
2. https://micchie.net/files/prism-nsdi21.pdf
3. https://marioskogias.github.io/docs/zygos.pdf

## Questions to ask:
1. Should I dicuss basic networking (how TCP or UDP works?) - and as a result discuss benefits of TLS for industry?
2. Is there any need for an explanation for FCFS?
