# Novel Sorting Algorithms via Threshold Decomposition  
## A Boolean Matrix Framework for Order Statistics and Selection

This repository implements a **Boolean logic–based framework** for sorting and order-statistic computation derived from the thesis *“Novel Sorting Algorithms Using Threshold Decomposition.”*

The central result of this work is that **median, p-th maximum, p-th minimum, weighted median, and even full sorting** can be computed using **Boolean operations alone**.  
Instead of direct element-to-element comparison, the framework uses **threshold dominance evaluation**, reformulating ordering as a **structural property of logical representations**.

---

## Core Idea

Given a dataset

A = {a₁, a₂, …, aₙ}

For each integer threshold t, define a Boolean variable:

Xᵢ(t) = 1  if aᵢ ≥ t  
Xᵢ(t) = 0  otherwise

Each threshold produces a Boolean dominance row indicating which elements survive that level.

As the threshold increases, the number of surviving elements monotonically decreases.

By stacking these rows, we obtain a **Boolean dominance matrix**.

Order statistics are recovered by analyzing **row-level dominance behavior**.  
Selection is therefore reformulated as a **vertical aggregation problem across dominance layers**, instead of a positional comparison problem.

---

## Hybrid Adaptive Distinct Set (ADS) Optimization

A naive approach evaluates all integer thresholds from 0 to MAX, resulting in:

O(N × MAX)

The **Hybrid Adaptive Distinct Set (ADS)** optimization observes that structural transitions occur only at distinct input values.

Let

T = {τ₁ < τ₂ < … < τᵣ}

be the sorted set of distinct values in the dataset.

Each threshold is assigned an interval width:

wₖ = τₖ − τₖ₋₁

All intermediate thresholds produce identical Boolean rows and therefore contain no new information.

This reduces the complexity to:

O(N × R)

where R is the number of distinct values.

For sparse datasets, this significantly reduces computational cost while preserving exact correctness.

---

## Boolean Selection Rules

At each threshold τ:

ones  = number of elements ≥ τ  
zeros = N − ones

Selection conditions are expressed purely as Boolean dominance rules:

- Median condition  
  ones > zeros

- p-th maximum condition  
  ones ≥ P

- p-th minimum condition  
  zeros < P

The final statistic is reconstructed using:

Result = Σ wₖ · V(τₖ)

where V(τₖ) is a Boolean indicator specifying whether the threshold satisfies the required selection rule.

This produces the exact order statistic without explicit comparison operations.

---

## Weighted Median

For weighted datasets, each element aᵢ has an associated positive weight wᵢ.

Total weight:

W_total = Σ wᵢ

The weighted median is defined as the smallest value whose cumulative weight is at least:

W_total / 2

The thesis establishes that:

- The weighted median reduces to the ordinary median when all weights are equal.
- Weighted selection is equivalent to computing the median of a logically expanded multiset.
- The Boolean threshold framework remains structurally valid in the weighted setting.

This demonstrates theoretical consistency between weighted and unweighted formulations.

---

## Sorting via Boolean Selection

Sorting can be expressed as repeated Boolean selection:

1. Extract the minimum (p-th minimum with P = 1)
2. Remove or mark the selected element
3. Repeat

Thus, full sorting becomes a sequence of Boolean dominance resolutions.

This shows that ordering operations are reducible to logical aggregation rather than arithmetic comparison.

---

## Hardware and Parallel Relevance

The framework is particularly aligned with hardware-oriented computation:

- Boolean operations map directly to logic gates
- Threshold evaluations can be parallelized
- Bit-vector representations enable wide logical operations
- No complex arithmetic units are required

In architectures emphasizing parallelism or hardware specialization, Boolean dominance evaluation can offer structural advantages.

---

## Repository Structure


src/
├─ hybrid_ads_boolean.py
└─ weighted_median.py

docs/
└─ thesis.pdf

examples/
└─ demo.py


---

## Research Positioning

This work connects:

- Order statistics theory  
- Threshold logic  
- Boolean matrix representations  
- Hardware-conscious algorithm design  

It extends ideas historically used in median filtering and threshold logic into a generalized framework for sorting and selection.

The broader contribution is conceptual: numerical ordering can be reformulated as a logical dominance problem without loss of correctness or interpretability.

---

## Author

**:contentReference[oaicite:0]{index=0}**  
Department of Computer Science and Engineering  
**:contentReference[oaicite:1]{index=1}**

Under the supervision of  
**:contentReference[oaicite:2]{index=2}**
