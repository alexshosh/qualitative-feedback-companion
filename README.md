# Qualitative-behaviour control with uncontrollable linearisation: branching feedback and the geometry of its singularity locus

Alex Shoshitaishvili (also published as A. N. Shoshitaishvili), Independent Researcher

<!-- DOI badge to be added after the first Zenodo release -->

## Abstract

The qualitative-behaviour control (QBC) problem is to make the closed loop reproduce a behaviour smoothly equivalent to a given one. At a working point where the linearisation of the plant is uncontrollable, this problem has no smooth solution if the spectrum of the given behaviour does not contain some uncontrollable eigenvalue. We show what can be done instead. The plant (state x) is coupled to a reference system (state z) by a coupling law u(x,z), and one looks for a surface x = F(z) that the joint motion keeps invariant. If the reference does not share an uncontrollable eigenvalue of the plant, F is singular at the working point, F^(-1)(x) has several points z for some x, and u(x,F^(-1)(x)) is a branching feedback. Its branches correspond to regions of the surface x = F(z) (most often adjacent), and a switching law defines the change of branch. We consider branching QBC after the author's papers of 1988-1992 and introduce two new notions: ultrastability, the uniform stabilisation of every plant of a family that may include plants with no smooth stabiliser, as when an actuator fails; and robust ultrastability, the same with one feedback for the whole family. The new results are: stabilisation of x' = u^n, n >= 2; ultrastability and robust ultrastability for x' = u^n + xA(x,conj(x),u,conj(u)) + conj(x)B(x,conj(x),u,conj(u)) (as in damping of a family of resonators); an ultrastable and robust ultrastable Andronov-Hopf bifurcation as the target behaviour, for a part of this family (as for resonators with damping, detuning and a Duffing term); two stabilisers of the nonholonomic (Brockett) integrator, a branching one and a continuous time-periodic one; and an attracting cycle of prescribed frequency at an uncontrollable critical pair +-i omega_0, where no smooth feedback can change omega_0, for nondegenerate quadratic control terms, from an explicit range apart from a few resonances. The short version, without proofs, is the Core preprint; here we give the proofs and further results.

This is the full version; see also the short preprint *Branching feedback at an uncontrollable linearisation with applications to stabilisation, the Brockett integrator, control of frequency and Hopf bifurcation* (10 pages), [doi:10.5281/zenodo.23847218](https://doi.org/10.5281/zenodo.23847218).

## Files

- `Shoshitaishvili_QualitativeFeedback_Companion.tex` - LaTeX source (amsart; Figure 1 is inline TikZ).
- `Shoshitaishvili_QualitativeFeedback_Companion.pdf` - compiled preprint (pdflatex, 57 pages).
- `figure_blowup.png` - Figure 2, the blow-up of the Brockett integrator.

## Building

```
pdflatex Shoshitaishvili_QualitativeFeedback_Companion.tex
pdflatex Shoshitaishvili_QualitativeFeedback_Companion.tex
pdflatex Shoshitaishvili_QualitativeFeedback_Companion.tex
```

## Citing this work

See [`CITATION.cff`](CITATION.cff).

## License

Creative Commons Attribution 4.0 International (CC BY 4.0)

Copyright (c) 2026 Alex Shoshitaishvili
