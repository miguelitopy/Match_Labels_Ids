# Match_Labels_Ids

📦 System Overview:
This Python-based system is designed to monitor and validate label information throughout the production workflow. It performs real-time reading, processing, and comparison of label data to detect matches and mismatches between expected and scanned values. These checks ensure accuracy and consistency in product identification and traceability.

🔌 Communication Protocol:
The system interfaces directly with industrial scanners manufactured by Keyence, utilizing Socket programming over TCP/IP to establish a stable and high-speed data exchange. This enables seamless integration with automated production lines, allowing instant feedback, error detection, and process adjustments based on label verification outcomes.

🔧 Technologies Involved:
- Keyence SR-1000 Series Scanners: High-performance industrial code readers used for capturing barcode and label data with precision and speed. These scanners feature integrated lighting and autofocus capabilities, ensuring reliable detection even in challenging conditions on the production line.
- Socket-Based Communication: The system communicates with the scanners and controllers using standard TCP/IP socket protocols, enabling fast, real-time data exchange and seamless integration into automated environments.
- LS Brand PLCs: Programmable Logic Controllers (PLCs) from LS Electric are used to manage and coordinate industrial operations. They serve as the backbone of the automation process, facilitating synchronized control between machinery, scanners, and the Python system.

<img width="914" height="538" alt="image" src="https://github.com/user-attachments/assets/b1eaf579-011c-4181-af6a-b19976a1af68" />



