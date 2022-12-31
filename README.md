# RPC-scheduler

### This repository is used for my MEng Individual Project at Imperial College London

## Introduction
Tail latency is vital for vendors that want to provide guarantees to their clients, which is particularly hard to control when dealing with RPCs (remote procedure calls) at the µs scale. Current solutions utilise streaming or datagram-based transport protocols for RPCs that impose overheads and limit the design flexibility, which is where innovations such as R2P2[1] build on top of UDP to overcome this. However, custom/UDP-based protocols are currently not enough to convince industry partners to move away from a more secure and well-known TCP solution. 

My project aims to convince industry to adopt more sophisticated ways of using or building on top of TCP so that we can reap similar benefits shown in R2P2[1] while not sacrificing security. It has been previously shown that a TCP-based solution can be used, specifically in object storage [2], to reduce the overhead in the typical frontend proxy architecture deployed in industry.  

## Background
### Datacenter RPCs
#### High-Performance vs Warehouse-Scale Computing [4]:
A key emphasis in warehourse-scale computing systems is the need to optimise for low latencies while achieving greater utilisation High-performance workloads tend to have simpler and static data structures that lend themselves to simpler, faster networking. It is emphasised for pure performance, while warehouse-scale systems focus on the performance-per-total-cost-ofownership in large-scale Web deployments. As a result, high-performance systems can afford to trade throughput for latency. 

### RPCs Contribution to Datacenter Tax [4,5]:
In each datacenter there are common procedures across applications that constitutes a significant fraction of total datacenter cycles. This is referred to as "datacenter tax", which is what datacenters seek to improve the most as it will provide the biggest impact. The components that are typically included in the tax classification are: protocol buffer management, remote procedure calls (RPCs), hashing, compression, memory allocation and data movement. 

With the demise of Dennard's scaling and slowing of Moore's law, we observe how cloud companies instead have increased the number of computers they use in a customer query to enhance online services. For instance, single-user search query already turns into thousands of remote procedure calls, a number that will increase in the future. My work takes this into consideration by aiming to increase the throughput and decrease latency of the datacenter prevelent RPCs that is part of the tax.

### Looking at the Tail [6,7]
Analysing the tail latency has become vital to cloud companies, since it allows them to observe whether all customers are satisfied. This is the reason why clients and services engage in service level agreements (SLAs), a formally negotiated contract where a client and a service agree on several system-related characteristics, typically including a high expected request rate distribution alongside an expected service latency under those conditions. 

Cloud companies as a result of needing to decrease latency tend to parallelize sub-operations across many different machines, where each sub-operation is co-located with its portion of a large dataset. Parallelization happens by fanning out a request from a root to a large number of leaf servers and merging responses via a request-distribution tree. These sub-operations must all complete within a strict deadline for the service to feel responsive. The decision of which leaf server to send a request to has a massive impact on service time variability which in turn has an effect on latency. This effect is further amplified when typical datacenters have multiple layers of routing/load-balancing within. With the help of queueing theory, we are able to understand how to tackle workloads with simple and varied service time distributions - avoiding head-of-line blocking which affects the latency of a request. 

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

### Load Balancing
Load balancers encapsulate a set or worker nodes behind a single virtual IP address with the aim of providing high availability. They have the responsibility to deciding which node to serve the request it recieves, which has an effect on tail-latency and throughput (as mentioned in the previous section). Load balancers can be implemented in either software or in hardware instead and can be identified in either the layer 4 and layer 7 load balancer categories.

#### Layer 4 [1]
Layer 4 (also referred as 'network') load balancers operate at the transport-level of the OSI model by using the 5 tuple information of TCP or UDP flow to make a decision on which worker node to assign the request to. The assign is static and independent of the load.

#### Layer 7

### Current Architectures
#### Issues with Reverse Proxy Architecture [2]:
Industry typically uses a reverse proxy architecture to handle the routing of RPCs within their service mesh. Usually, this is done using a frontend server (such as NGINX) that recieves the request from a client and forwards it to at least one of the backend servers. In this architecture, the frontend server compute resources are being fully utilised, while the backend servers' resources are under-utilised. As a result, this design suffers in terms of throughput. 

#### Issues with Application-Aware Architectures [2]:
Recent progress have introduced the use of content-based routing architectures where the backend servers interact with programmable switches. This results in an improvement in throughput, latency, and resilience to skew (which is prevalent in realistic workloads), due to the switch's ability to redirect traffic that would otherwise be arriving at congested backend nodes. 

Although this is promising, the biggest issue it faces is that these solutions are UDP-based. This restricts clients to using a custom UDP-based protocol where they would implement loss recovery and congestion control functionality themselves, which is a non-trivial task. In addition, since it does not fuly support TCP it lacks support for industry standrd TLS security or popular application-level protocols. As a result, despite it's great progress in the academic field, industry is not keen to adopt it yet. 

## Project Plan

## Evaluation Plan

## Ethical Issues

## References
1. https://www.usenix.org/system/files/atc19-kogias-r2p2_0.pdf
2. https://micchie.net/files/prism-nsdi21.pdf
3. https://marioskogias.github.io/docs/zygos.pdf
4. https://dl.acm.org/doi/pdf/10.1145/3015146
5. https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/44271.pdf
6. https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf
7. https://www.barroso.org/publications/TheTailAtScale.pdf
