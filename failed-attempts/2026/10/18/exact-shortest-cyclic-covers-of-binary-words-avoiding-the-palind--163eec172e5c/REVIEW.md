# Independent mathematical audit

## correctness

PASS

A host is a closed walk in the full binary overlap graph. Subtracting one of each required edge leaves a nonnegative integral flow with unit supplies at the allowed suffix-01 vertices not starting 10 and demands at their reversals. Paths from a supply have length at least j, the first internal 10 position, or n−1 for 0^(n−1)1 (n=k−1). The routing 0^a1^b s → s1^b0^a is admissible at its endpoint: the appended ones extend the terminal 1 of s before any zeros arrive. Its image is uniquely invertible by the trailing zero run and one run; the exceptional route to 10^(n−1) cannot collide because the ordinary images have more than one 1. This realizes all lower bounds; the base graph is strongly connected by routing via 1^n, so the balanced augmentation admits an Euler circuit. In any equality case the special supply path has n−1 shifts, which require appended first bit 0 to get destination prefix 10. Since the initial vertex ends 01, every minimum host contains 010. The four-state walks from 10 to 01 give z³(1−z)/D(z), D=(1−z)²−z³. Weighting the prefixes by a+b and adding the exceptional costs yields the claimed E series. The three-state prefix automaton gives (1+z²)/D, with primitive adjacency and a simple dominant pole alpha; the ratio follows by evaluating the numerators there. The bounded independent BFS/min-cost-flow computation matched E_k for k=3..10 and found constrained overheads E_k+1 on that range. The general conclusions use the proof, not that finite check.

## originality

FAIL

Distinct Resultary entry c88f5aa31843 covers precisely the same linear-avoidance language, single cyclic host with repeated and forbidden windows, and all-order minimum and overhead series. Its per-deficit lower bound and equality construction also imply the forced forbidden factor. Complementation and the overhead ratio are mechanical. This is indexed mathematical coverage, not an attribution or conclusion about which result was obtained first; the matched catalogue entry has a later displayed date.

## value

PASS

As a theorem this is an informative exact solution to a natural route-balancing problem: a single structured matching simultaneously attains all individual path lower bounds for an infinite family, and equality distinguishes host avoidance from required-window avoidance. This usefulness does not supply a distinct contribution once the equivalent exact indexed theorem is accounted for.

The dated certificate retains the supplied scientific assessment, sources and limitations.
