# ISO 27000-Series Framework Project

## Introduction to ISO 27000 Series
The ISO/IEC 27000-series comprises information security standards published by the International Organization for Standardization (ISO) and the International Electrotechnical Commission (IEC). The series provides best practice recommendations on information security management, risks, and controls within the context of an overall Information Security Management System (ISMS).

## Key Standards
- **ISO/IEC 27001**: Specifies the requirements for establishing, implementing, maintaining, and continually improving an ISMS.
- **ISO/IEC 27002**: Provides guidelines for organizational information security standards and information security management practices.
- **ISO/IEC 27005**: Provides guidelines for information security risk management.

## Applying the ISO 27000 Series to This Project
This project demonstrates how to create and manage an ISMS based on the ISO 27000 series standards using open-source tools on Ubuntu. Here’s a detailed explanation of each component and how it aligns with the ISO 27000 series framework:

### 1. Scope of ISMS (`scope.md`)
ISO 27001 Requirement: Define the boundaries and applicability of the ISMS within the organization.

#### Application:
- Document: `scope.md`
  - Content: Specifies what parts of the organization the ISMS covers, ensuring clarity on which assets, processes, and systems are included.

### 2. Information Security Policy (`information_security_policy.md`)
ISO 27001 Requirement: Establish an information security policy that provides management direction and support for information security.

#### Application:

- Document: `information_security_policy.md`
  - Content: Outlines the organization’s commitment to information security, sets objectives, and provides guidelines for achieving these objectives.

### 3. Risk Assessment and Management (`risk_assessment.md`)
ISO 27005 Requirement: Identify, analyze, and evaluate information security risks.

#### Application:

- Document: `risk_assessment.md`
  - Content: Describes the risk assessment process, identifying assets, threats, vulnerabilities, impacts, and likelihoods to determine the risk levels.

### 4. Implementing Controls (`controls.md`)
ISO 27002 Requirement: Implement information security controls to mitigate identified risks.

#### Application:

- Document: `controls.md`
  - Content: Lists the security controls implemented to mitigate identified risks, following guidelines from ISO 27002.

### 5. Monitoring and Reviewing the ISMS (monitoring.py and review.md)
ISO 27001 Requirement: Monitor and review the ISMS to ensure its effectiveness and compliance with the security policy.

#### Application:

- Script: `monitoring.py`
  - Content: Python script to monitor the status of critical services, ensuring they are running as expected.

- Document: `review.md`
  - Content: Describes the review process for the ISMS, ensuring it is periodically reviewed for effectiveness and improvements.

### 6. Continuous Improvement (improvement_plan.md)
ISO 27001 Requirement: Continually improve the ISMS to enhance information security performance.

#### Application:

- Document: `improvement_plan.md`
  - Content: Contains a plan for continuous improvement, addressing any identified gaps or weaknesses in the ISMS.

### 7. Assets Management (assets.py and assets.txt)
ISO 27001 Requirement: Identify and manage information assets.

#### Application:

- Script: `assets.py`
  - Content: Python script to list all information assets.

- Output: `assets.txt`
  - Content: Generated list of assets.

### 8. Project Overview (README.md)
ISO 27001 Requirement: Document the ISMS and make relevant documentation available to stakeholders.

#### Application:

- Document: `README.md`
  - Content: Provides an overview of the project, instructions for setting up and running the project, and additional project details.

## Coding
### `monitoring.py`
The `monitoring.py` script is designed to check if certain services are running on your Ubuntu system.

#### Importing
- The `os` module in Python provides a way to interact with the operating system. In this script, it is used to run system commands.

#### Defining the Function
- The `check_services` function is responsible for checking the status of the specified services.

#### List of Services to Check
- A list of service names that you want to check. In this script, it includes `ssh` and `apache2`.

#### Looping Through the Services
- The script loops through each service in the `services` list.
- `os.system(f"systemctl is-active --quiet {service}")` runs the system command systemctl is-active --quiet <service>.
- The `systemctl is-active --quiet` command checks if a service is active without producing output. If the service is active, it returns `0`; otherwise, it returns a non-zero status.

#### Checking the Service Status
- If the status is not `0`, it means the service is not running.
- The script prints a message indicating which service is not running.

#### Main Execution Block
- This block ensures that the `check_services` function is called only when the script is run directly (not when imported as a module).

### `assets.py`
The `assets.py` script is designed to list information assets and write them to a text file. 

#### List of Information Assets
- A list of information assets. In this example, it includes `Server1`, `Database1`, `Workstation1`, and `Router1`.

#### Writing Assets to a File
- `with open('assets.txt', 'w') as f`: This opens the file `assets.txt` in write mode. If the file does not exist, it will be created. The with statement ensures the file is properly closed after the block of code is executed.
- `for asset in assets`: This loops through each asset in the `assets` list.
- `f.write(f"{asset}\n")`: This writes the asset to the file, followed by a newline character. The `f` string formatting is used to include the asset name in the string.

## Summary

This project is designed to demonstrate the practical application of the ISO 27000-series standards in establishing, implementing, maintaining, and continually improving an Information Security Management System (ISMS). It covers defining the ISMS scope, creating an information security policy, conducting risk assessments, implementing controls, monitoring, reviewing, and continually improving the ISMS. Each component is aligned with the requirements of the ISO 27000 series, providing a comprehensive framework for managing information security within an organization.
