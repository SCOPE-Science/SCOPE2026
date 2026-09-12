"""Verify the 2-step uniform->uniform map numerically, then confirm 4-step closure + prefactors.
Family A (uniform): faces (u,u,u,u)/(v,v,v,v) checkerboard.
Family B (cross): faces (p,q,q,p) checkerboard-flipped: even faces (p,q,q,p), odd (q,p,p,q).
Step A->B: (x,y) -> (1/(2x), 1/(2y)) [from iso2: even parent x gives new X=1/(2x)=p].
Step B->A: need map. Take B-faces (p,q,q,p): cyclic (p,q,q,p): a=p,b=q,c=q,d=p: Delta = pq+qp = 2pq. Inner: W_k = w_{k+2}/D: (q,p,p,q)/(2pq) = (1/(2p), 1/(2q), 1/(2q), 1/(2p)).
New faces at old vertices → uniform? Verify numerically: build B-pattern Aztec, shuffle, iso-read faces.
"""
from general_shuffle import build_general, uniform_face, shuffle_general, reduce_g, raw
from validate_ops import brute_Z
from iso2 import *  # noqa -- runs heavy code; instead inline below
