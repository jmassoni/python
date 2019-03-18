# The Power of Two Choices

## Flexible Deadline (because codeanywhere is ruining our lives)

I'll ask you to turn this in the week after we return from Fall Break, but I'm not setting a mandatory deadline because of the difficulty we've been having with the development environment.

## Description

Use the discrete event time-advance strategy to model a machine repair system with two single-server queues in **parallel**.

When a machine breaks, it waits for repair in one of the two queues. The queues operate independently, so both can be repairing machines at the same time.

Assume that machine lifetimes are geometrically distributed with parameter *p* = .10 and that repair service in either queue takes a deterministic 5 units of time. These are the same parameters used in our in-class example. Machines wait in the queue in first-come-first-serve order.

Write two different versions of the simulation:

- In the first, customers join a **randomly chosen** queue.

- In the second, customers join **the shortest queue**. If the two queues have equal length, choose one at random.

In both cases, estimate the average residence time in the system as a function of the number of machines *N*.

In addition to the code, turn in a plot made with `matplotlib` showing how the average residence time changes under each of the two cases as the number of machines increases from *N* = 2 to *N* = 10.

## Tips

Use the `machine_repair.py` code as a starting point, included in this repo.

Most of the code needs only minor changes. You need to think about the section that processes events in light of the fact that there are now two queues and two different rules for joining the queues. I recommend starting by designing flowcharts like we discussed in class.

Take a look at Allen Downey's [*Think Python* book](https://greenteapress.com/wp/think-python/). The chapters on tuples and dictionaries may be helpful.





