# CodeRipple Test Repository

This repository is designed specifically for testing the CodeRipple automated code analysis system.

## Purpose
- Validate end-to-end pipeline functionality
- Test real AI analysis with Strands + Claude 3.5 Sonnet
- Demonstrate CodeRipple capabilities

## Structure
- `main.py`: Entry point with core functionality
- `utils.py`: Utility functions for analysis depth
- `requirements.txt`: Python dependencies

## Expected Analysis
This repository should trigger comprehensive AI analysis including:
- Code structure analysis
- Function documentation
- Dependency analysis
- Architecture insights

## Testing Workflow
1. Push changes to trigger CodeRipple webhook
2. Monitor pipeline execution across all components
3. Validate analysis results in Showroom
4. Check event logging in Cabinet

**CodeRipple Webhook**: Configured to analyze this repository automatically on push events.


## Pipeline Testing

This change triggers the CodeRipple end-to-end pipeline test.

**Test Timestamp**: Tue Jul  1 15:16:28 NZST 2025
**Expected Flow**: GitHub webhook → Receptionist → Analyst → Deliverer → Showroom


**Integration Fix Applied**: Tue Jul  1 15:22:30 NZST 2025
- API Gateway now properly integrated with Receptionist Lambda
- Webhook should trigger complete pipeline
