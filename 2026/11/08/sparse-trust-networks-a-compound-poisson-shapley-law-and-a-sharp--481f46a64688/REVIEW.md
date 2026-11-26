# Independent mathematical audit

## correctness

PASS

The external game of a head k is the difference of its singleton unanimity game and the one requiring k and all its in-neighbors. An internal arc contributes half to each endpoint. This gives the stated h(d^-) plus t(d_j^--1) for each outgoing destination. Conditional on the root's outgoing arcs, the residual incoming counts at different destinations use disjoint columns excluding the root row, independent also of the root indegree. Nonnegativity gives the exact zero probability; efficiency gives the mean. At n=2 the mark is identically zero; the edge-probability endpoints also agree. The binomial limits and a tight number of marks give the tagged law, with the compound-Poisson component independent of h(P^-); positive credit and zero credit can be tested on the limiting integer data. The stated mean also follows from bounded second moments of the two root degrees, and the stated variance from conditioning on the Poisson number of marks. For the empirical part, line 85's informal exploration can be made exact without claiming conditional independence of all revealed absences: first expose the two roots' outgoing rows. The outside-root sources in the two root columns give independent Bin(n-2,p_n) indegrees, omitting the two arcs between roots. At each outside destination its incoming count from outside the two roots is an independent Bin(n-3,p_n) mark, independent of both rows and root columns. Use independent replacement marks for the second root at any common destination; the two resulting ideal payoffs are independent, because conditional on the rows their marks have the same product laws at all specified destinations and the rows determining their counts are independent. The original pair differs only if a root-to-root arc is present or an outside destination is shared, of probability at most 2p_n+(n-2)p_n². This proves asymptotic pair independence of bounded tests and zero indicators, hence empirical weak convergence by the variance bound and tightness. At the threshold the exact zero-to-isolation ratio is 1+o(1) while n times isolation probability tends to e^(-t); Markov transfers the isolate limit to W_n. The directed factorial moment exponent counts both cross arcs and internal arcs once, and yields the Poisson law. The subcritical second moment for isolates and supercritical first moment of W_n give the stated two sides.

## originality

PASS

The game and deterministic Shapley formula are prior work as explicitly credited. The supported distinct contribution is the joint stochastic characterization: exact finite tagged distribution, its limiting sparse empirical payoff law, and the sharp equality in probability between zero-credit and isolated vertex counts in the critical window. The isolated-vertex Poisson limit itself is not new.

## value

PASS

The exact law separates internal credit at a root and the contribution from redundant incoming support at its neighbors. It yields an explicit positive atom at zero and an empirical profile despite correlated allocations. That atom is strictly larger than the isolation fraction in the bounded-degree limit, whereas the delicate disappearance window is governed by isolation alone. This regime distinction is substantive; the result is not a recomputation of the classical isolate count or deterministic Shapley identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
