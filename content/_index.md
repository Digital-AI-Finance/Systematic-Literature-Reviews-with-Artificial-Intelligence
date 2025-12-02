---
title: "Systematic Literature Reviews with AI"
description: "Comprehensive resources, tools, and research for conducting Systematic Literature Reviews using Artificial Intelligence and Large Language Models"
---

<section id="overview">

## Overview

Systematic reviews constitute a critical foundation for evidence-based decision-making across disciplines. However, the labor-intensive nature of traditional SLRs - requiring weeks to months of manual work - has driven significant interest in AI-assisted automation.

### Key Statistics

| Metric | Value |
|--------|-------|
| Workload reduction with AI screening | **40-95%** |
| otto-SR: Cochrane reviews completed | **12 reviews in 2 days** (vs ~12 work-years manually) |
| GPT-4 PICO extraction accuracy | **>85% median** |

</section>

---

<section id="tools">

## AI Tools for Systematic Reviews

### Open Source Tools

{{< tool-table type="open" >}}

### Commercial & Freemium Tools

{{< tool-table type="commercial" >}}

### Specialized LLM Applications

{{< llm-apps >}}

</section>

---

<section id="papers">

## Key Research Papers

### Foundational Papers

{{< paper-list category="foundational" >}}

### Recent LLM Research (2024-2025)

{{< paper-list category="llm" >}}

### Methodology & Guidelines

{{< paper-list category="methodology" >}}

</section>

---

<section id="guidelines">

## Methodological Guidelines

### PRISMA-AI Framework

The PRISMA-AI extension provides standardized reporting for AI-related systematic reviews:

- Search strategy documentation
- Quality assessment with AI-specific criteria
- Transparent result reporting
- Technical reproducibility requirements

### LLM Integration Guidelines

When integrating LLMs into systematic reviews:

#### 1. Screening Phase
- Use zero-shot or few-shot classification
- Define clear inclusion/exclusion criteria in prompts
- Maintain human oversight for borderline cases

#### 2. Data Extraction
- Use structured prompts (RISEN framework)
- Validate extracted data against source documents
- Document prompt versions for reproducibility

#### 3. Quality Assurance
- Dual verification (AI + human) recommended
- Report sensitivity and specificity metrics
- Document AI model versions and parameters

</section>

---

<section id="benchmarks">

## Performance Benchmarks

### Screening Accuracy

{{< benchmark-table type="screening" >}}

### Data Extraction

{{< benchmark-table type="extraction" >}}

### Time Savings

{{< benchmark-table type="time" >}}

</section>

---

<section id="resources">

## Additional Resources

### Getting Started

**For Beginners:**
1. **Start with Rayyan** - Free tier, user-friendly interface
2. **Try ASReview** - Open source, well-documented
3. **Read the PRISMA guidelines** - Understand methodological requirements

**For Advanced Users:**
1. **Explore otto-SR** - State-of-the-art LLM automation
2. **Build custom GPT extractors** - Use RISEN framework
3. **Combine tools** - ASReview for screening + ChatGPT for extraction

### Key GitHub Repositories

- [asreview/asreview](https://github.com/asreview/asreview) - Active learning for systematic reviews
- [asreview/synergy-dataset](https://github.com/asreview/synergy-dataset) - ML dataset for study selection
- [systematic-reviews topic](https://github.com/topics/systematic-reviews) - GitHub topic for SLR tools

### Library Guides

- [King's College London - AI in Evidence Synthesis](https://libguides.kcl.ac.uk/systematicreview/ai)
- [Purdue University - AI Tools for Systematic Review](https://guides.lib.purdue.edu/c.php?g=1371380&p=10619604)
- [Harvard Library - Systematic Reviews Software](https://guides.library.harvard.edu/meta-analysis/software)
- [Lancaster University - Systematic Reviews Tools](https://lancaster.libguides.com/SystematicReviews/tools)

### Python Quick Start

```python
# Install ASReview
pip install asreview

# Basic usage
from asreview import ASReviewProject

# See documentation: https://asreview.readthedocs.io/
```

</section>

---

<footer>

*Last updated: December 2025*

**Repository:** [Digital-AI-Finance/Systematic-Literature-Reviews-with-Artificial-Intelligence](https://github.com/Digital-AI-Finance/Systematic-Literature-Reviews-with-Artificial-Intelligence)

</footer>
