# Independent mathematical audit

## correctness

PASS

For an isolated cluster, until its first positive idle gap the available work just before release j is the previous service sum minus d_j (with coincident events processed together). Thus cover is exactly continuous service to B. The first violation instead ends the first busy interval at a proper partial sum <B. In the combined staggered queue, adding arrivals to an isolated cluster's input cannot decrease reflected workload; every primary t_i before the end tau of a busy interval therefore has t_i+B_i<=tau if tau is finite. Each release is strictly before t_i+B_i since all service sizes are positive. Thus at tau no trigger from that busy interval is pending. From the common empty start a, batch cumulative work up to a candidate first end v is at least staggered cumulative work. If batch ended strictly earlier, its cumulative work at v would be v-a, incompatible with continued staggered service through v and positive workload there. If staggered ends at finite tau, each of its primaries' full work has arrived, so batch also clears at tau; if staggered never ends no earlier batch end is possible. Repeat from the common empty state. This uses ends followed by a positive gap, not left-limit zeros at immediate restarts, and allows simultaneous primaries. Under Poisson input, conditional on a failing initial mark the event of no further primary until d_last+B+1 has positive probability and isolates the failure; countably many a.s.-covered marks give sufficiency. The batched service tree has conditionally Poisson(lambda B) offspring, giving the stated transform; rho<1 gives a finite tree and a transform fixed point unique by a Lipschitz bound rho. Summing expected work by generation gives EB/(1-rho), fresh Poisson increments at true clearings give independent exponential idle times, and for constant service the PGF solves F=z exp(rho(F-1)), giving the Borel formula by Lagrange inversion and L=bK.

## originality

PASS

The strongest actual precursor is Inoue–Takine's exact busy-indicator equivalence for periodic cell trains, not merely a similar stochastic bound. The supported distinct claim is the sharp cumulative-service criterion for arbitrary locally finite primary schedules and finite heterogeneous clusters, together with the Poisson a.s. iff and resulting batch reduction. The classical transforms themselves are not new.

## value

PASS

A simple markwise condition removes all intra-cluster timing information from an exact cycle law, with a sharp isolated witness rather than a sufficient approximation. It applies to heterogeneous services and dependent delays, can accept triggers after primary service, and makes classical batch formulas valid for the coupled staggered system. The structural reduction, not rederivation of Borel probabilities, provides the research value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
