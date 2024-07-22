# ISO 27000-Series Framework Project

This project implements an Information Security Management System (ISMS) based on the ISO 27000-series standards using open-source tools on Ubuntu.<br>
<a href="https://github.com/MenakaGodakanda/iso27000-framework/blob/main/Project_Description.md">Project Description</a>

## Overview

<img width="1044" alt="Screenshot 2024-07-21 at 3 39 00 PM" src="https://github.com/user-attachments/assets/5fd96cff-791b-417c-90f1-7fbde046e2dc">

### Explanation
#### 1. ISMS Scope (`scope.md`):
- Defines the boundaries and scope of the ISMS. (<a href="https://github.com/MenakaGodakanda/iso27000-framework/blob/main/scope.md">scope.md</a>)

#### 2. Information Security Policy (`information_security_policy.md`):
- Establishes the overall security policy and sets the direction for information security management (<a href="https://github.com/MenakaGodakanda/iso27000-framework/blob/main/information_security_policy.md">information_security_policy.md</a>).

#### 3. Asset Management (`assets.py`, `assets.txt`):
- assets.py: Script to identify and list all information assets (<a href="https://github.com/MenakaGodakanda/iso27000-framework/blob/main/assets.py">assets.py</a>).
- assets.txt: Output of the `assets.py` script containing the list of assets (<a href="https://github.com/MenakaGodakanda/iso27000-framework/blob/main/assets.txt">assets.txt</a>).

#### 4. Risk Assessment (`risk_assessment.md`):
- Evaluates risks associated with the identified assets and documents them (<a href="https://github.com/MenakaGodakanda/iso27000-framework/blob/main/risk_assessment.md">risk_assessment.md</a>).

#### 5. Controls Implementation (`controls.md`):
- Implements security controls to mitigate the identified risks (<a href="https://github.com/MenakaGodakanda/iso27000-framework/blob/main/controls.md">controls.md</a>).

#### 6. Monitoring and Review (`monitoring.py`, `review.md`):
- monitoring.py: Script to monitor the status of critical services (<a href="https://github.com/MenakaGodakanda/iso27000-framework/blob/main/monitoring.py">monitoring.py</a>).
- review.md: Documents the review process of the ISMS to ensure its effectiveness (<a href="https://github.com/MenakaGodakanda/iso27000-framework/blob/main/review.md">review.md</a>).

#### 7. Continuous Improvement (`improvement_plan.md`):
- Implements plans for ongoing improvement of the ISMS (<a href="https://github.com/MenakaGodakanda/iso27000-framework/blob/main/improvement_plan.md">improvement_plan.md</a>).

## Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/MenakaGodakanda/iso27000-framework.git
    cd iso27000-framework
    ```

2. Run the `assets.py` script to generate the list of assets:
    ```bash
    python3 assets.py
    ```

3. Run the `monitoring.py` script to check the status of services:
    ```bash
    python3 monitoring.py
    ```

## Project Structure

```
iso27000-framework/
├── assets.py
├── assets.txt
├── controls.md
├── improvement_plan.md
├── information_security_policy.md
├── monitoring.py
├── README.md
├── review.md
├── risk_assessment.md
├── scope.md
```

- `scope.md`: Defines the scope of the ISMS.
- `information_security_policy.md`: Contains the Information Security Policy.
- `risk_assessment.md`: Documents the risk assessment process.
- `controls.md`: Lists the implemented security controls.
- `monitoring.py`: Script to monitor the status of services.
- `review.md`: Contains the ISMS review process.
- `improvement_plan.md`: Continuous improvement plan for the ISMS.
- `assets.py`: Script to list information assets.
- `assets.txt`: Output of the `assets.py` script.

## License

This project is licensed under the MIT License.
