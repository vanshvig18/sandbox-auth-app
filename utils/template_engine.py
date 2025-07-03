def generate_document(template_type, data):
    if template_type == "ML Documentation":
        return f"""\
# ML Documentation

## Project: {data['project_name']}
**Author**: {data['author']}

### Description
{data['description']}

---
### Sections
- Data Collection
- Model Architecture
- Training & Evaluation
"""
    elif template_type == "SAR Repository":
        return f"""\
# SAR Report

## System Name: {data['project_name']}
**Prepared by**: {data['author']}

## Overview
{data['description']}

## Security Analysis
- Threat Modelling
- Mitigation Strategies
"""
    else:
        return "Invalid Template"
