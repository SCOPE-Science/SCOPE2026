# Independent mathematical audit

## correctness

PASS

In the zero-carryover specialization, adult escape leaves h/(1+y) as the prey input to recruitment, and juvenile survival divides recruited prey by 1+x. Multiplying juvenile consumption by its conversion and normalization gives x'=R_J x h'; the adult equation similarly gives y'=R_A y h/(1+y). On the stated capacity interval, G is positive and at most 1; hence the recurrence preserves positive coordinates and h≤1, and x_{t+1}≤R_J regardless of initial predator densities. Dividing the exact updates gives q_{t+1}=(R_A/R_J)q_t/(1+y_t), and y_t=R_J x_{t−1}q_t for t≥1. Strict inequality gives geometric decay since x_{t−1}≤R_J for t≥2. At equality, q decreases: if its limit is zero the same bound works; if its limit is positive then ∑log(1+y_t)=log(q_0/q_∞)<∞, so y_t→0. Equivalently, at equality 1/q_{t+1}−1/q_t=R_J x_{t−1} for t≥1. This controls arbitrary admissible trajectories, not just equilibria; a compact forward-invariant positive set would have y bounded below, which is impossible. In Beverton–Holt recruitment the prey update simplifies to rh/[(1+x)(1+y+(r−1)h)]. A positive fixed point first forces h=1/R_J by the juvenile equation and then 1+y=R_A/R_J and 1+x=rR_J/(R_A+r−1). Positivity of both predators gives R_J<R_A<1+r(R_J−1); this open interval requires R_J>1 and then h<1. Conversely these inequalities and substitution prove existence and uniqueness, with one coordinate zero at each wedge boundary. The rational witness (r,R_J,R_A)=(3,2,3) gives (1/2,1/5,1/2) by direct substitution.

## originality

PASS

The underlying sequence of predation, recruitment and replacement parameters is prior, as is global predator loss at that predator's own threshold R₀≤1. In particular the previously covered part R_A≤1 is not credited as new. Seno–Goyal's Lemma 6 is a necessary parameter ordering for a positive equilibrium in their exponential-escape example. The distinct conclusions here are global relative-ordering exclusion even when 1<R_A≤R_J (including equality), using the shape-one ratio, and the full necessary-and-sufficient shape-one Beverton–Holt equilibrium wedge, including its upper bound. The matched rare-invader and single-predator analyses do not imply these.

## value

PASS

The identity distinguishes replacement ability in isolation from competition on arbitrary time-dependent prey trajectories. It yields a global obstruction to positive recurrence even when both predators exceed their individual invasion threshold, and the equilibrium census exhibits an upper as well as lower adult-replacement bound for potential coexistence. These questions arise in the unmodified stage-specific model and are not a numerical parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
