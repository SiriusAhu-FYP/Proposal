### 1. **Feasibility of Human-Homomorphic Interfaces (GUI/GCC)**

**Description (Updated)**:
This section discusses the use of **human-homomorphic interfaces (GUI/GCC)** for achieving cross-platform compatibility, eliminating the need for game-specific APIs. The focus is on demonstrating how GUI-based interaction can create adaptable, dynamic AI systems that can seamlessly integrate into different games and platforms. These approaches are grounded in **legal move constraints**, **action representation formats**, and **state representation**, ensuring stability across different gaming environments. This enables a consistent user experience without the reliance on proprietary game APIs.

**Actual Points**:

* **Legal Move Constraints**: Using a restricted valid‑action set (legal move constraints) improves stability and reduces error accumulation in GUI‑based agents. For example, in the GCC setting introduced by CRADLE, the lack of specialized API access is handled by enforcing keyboard/mouse action validity, which the authors show leads to improved generalization across games. \cite{CRADLE2024}
* **Move Representation Format**: In the benchmark dataset provided by ORAK, the authors emphasise that action mapping and representation across diverse game environments is non‑trivial, affecting cross‑game generalisation. \cite{ORAK2023}
* **State Representation**: The UI‑Venus framework highlights the importance of structured output at multiple granularities (format/type/coordinates/content) when controlling UI elements via GUI, showing that clearer state/action representation improves reliability in agent behaviour. \cite{UI‑Venus2023}
* **Multi-modal Inputs**: V‑MAGE demonstrates that vision‑only inputs pose significant generalisation challenges for game‑playing agents (e.g., handling novel scenes or object tracking). \cite{V‑MAGE2024}

---

### 2. **Evaluation Protocols & Performance Metrics**

**Description (Updated)**:
This section covers the evaluation frameworks used to measure the performance of AI assistants in dynamic gaming environments. By analyzing metrics such as **pass@k**, **Invalid%**, and **Opportunity-Normalized Success (OAS)**, we can evaluate the AI's effectiveness, efficiency, and error rate. These metrics also guide the design of **scaffolding** and **feedback mechanisms** that enhance AI stability and reliability over time. Proper benchmarking and **task-specific performance metrics** are essential for evaluating AI systems in real-world gaming scenarios.

**Actual Points**:

* **pass@k**: Measures how many attempts an AI needs to successfully complete a task. This metric is commonly used in decision‑making tasks to track success across multiple attempts and is particularly useful for evaluating task performance over repeated trials (Benchmarking-VLA-VLM, 2025).
* **Invalid%**: Tracks errors by measuring the proportion of **invalid actions** taken by the AI, which helps identify problems in action selection. A higher **Invalid%** indicates the model struggles to produce valid outputs within the specified action space (Benchmarking-VLA-VLM, 2025).
* **Granular Skill Assessment**: The V-Mage framework uses "Unit Tests for Core Visual Abilities" to provide a granular assessment of an agent's specific skills, such as positioning, trajectory tracking, timing, and visual memory, rather than just a single success score. \cite{V-Mage, 2024}
* **Benchmarking and Task-Specific Metrics**: Systems like **ORAK** and **lmgame-bench** provide comprehensive frameworks for systematically evaluating AI performance across multiple game types and specific tasks, ensuring consistent, reliable results (lmgame-bench, 2023; ORAK, 2023).
* **Dynamic ELO System**: V-Mage introduces a **Dynamic ELO system** to address cross-game comparison, helping standardize agent performance across different games and environments (V-Mage, 2024).

---

### 3. **Agentic Modules and Stability in Long-Horizon Tasks**

**Description (Updated)**:
This part explores the **agentic modules** (planning, memory, reflection, skills) that help maintain long-term stability in AI companions. These modules are critical in mitigating **error accumulation** and ensuring the AI can function reliably over extended tasks. By combining these modules, the system can handle **complex, long-sequence decision-making**, providing a robust AI assistant that supports players through sustained gameplay without drifting off course.

**Actual Points**:

* **Planning and Reflection**:
  Combining **planning** (task decomposition) with **reflection** (self-correction) allows the assistant to adapt to evolving situations and fix mistakes during long sequences. Both **CRADLE (2024)** and **OS-Agents (2024)** highlight how **self-reflection** and **adaptive planning** modules improve task stability. Specifically, **CRADLE** discusses how planning can be adjusted iteratively during tasks, and **OS-Agents** mentions the benefits of planning that adapts based on **environmental feedback** (CRADLE, 2024; OS-Agents, 2024).
* **Memory**:
  Both **short-term memory** (e.g., recent actions) and **long-term memory** (e.g., learned strategies) help stabilize performance across long-term tasks. The **ORAK (2023)** and **lmgame-bench (2023)** papers highlight the importance of memory modules in preventing drift over extended periods. **lmgame-bench** specifically mentions **memory scaffolding** as essential for stabilizing performance in long-horizon tasks, while **ORAK** focuses on the integration of memory into task planning (ORAK, 2023; lmgame-bench, 2023).
* **Error Mitigation**:
  These modules prevent **task drift** and ensure the AI doesn't lose focus over long sessions. Both **lmgame-bench (2023)** and **OS-Agents (2024)** emphasize how memory, planning, and reflection modules help reduce error accumulation in long-term tasks. For instance, **OS-Agents** specifically mentions how the **feedback loop** can help the agent adjust its approach in real-time to mitigate task errors (lmgame-bench, 2023; OS-Agents, 2024).
* **Skill Curation**:
  A modular approach to task-solving that involves breaking down actions into atomic skills that can be recombined dynamically. CRADLE (2024) introduces the concept of "Skill Curation" as a core module, which allows for better handling of long-term, dynamic tasks by generating and updating relevant skills. This supports the agent's adaptability by enabling it to decompose complex tasks into manageable sub-goals. \cite{CRADLE, 2024}
* **Feedback and Task Segmentation**:
  The idea of **task segmentation**—splitting longer sequences into manageable sub-tasks—was emphasized as essential for improving agent performance in complex environments. Both **OS-Agents (2024)** and **CRADLE (2024)** highlight how breaking down tasks and using feedback loops improves decision-making and prevents task loss in long-horizon tasks. The segmentation helps in **long-term planning** by making tasks more manageable and adaptable in real-time (OS-Agents, 2024; CRADLE, 2024).
* **Self-Evolving Trajectory Alignment**: The UI-Venus (2025) report introduces a "Self-Evolving Trajectory History Alignment" framework. This method acts as a form of automated reflection; the agent re-evaluates its past actions, filters for successful "thought-action pairs," and then uses these optimized thoughts to refine its historical context. This iterative refinement of its own memory and reasoning is shown to lead to "more coherent planning" and better performance in complex, long-horizon UI tasks.

---

### 4. **Learning Paradigms for Robust Agent Training**

**Description (Updated)**:
This section presents the major learning paradigms that underpin the training of interactive game/GUI assistants. In particular, it emphasizes how **reinforcement‑fine‑tuning (RL‑finetune)**, **structured action generation**, and **iterative feedback/refinement loops** enable agents to learn in long‑horizon, dynamic environments, bridging the gap between single‑step action models and sustained interactive assistance.

**Actual Points**:

* **RL‑Finetuning**: Rather than rely solely on supervised imitation, modern agent systems apply RL‑based finetuning (or reinforcement fine‑tuning, RFT) on top of pretrained models, enabling adaptation to multi‑step tasks, reward sparsity, and interactive decision‑making (UI‑Venus 2025; AgentGym‑RL 2025; Improving Agent Behaviors 2024).
* **Structured Action Generation**: To reduce error and constrain the output space, agents generate actions in a **structured form** (e.g., JSON or discrete macro actions) rather than free‑form text; this improves reliability in game/GUI environments (UI‑Venus 2025).
* **Iterative Feedback/Refinement Loops**: Agents employ mechanisms such as **self‑evolving trajectories**, **progressive interaction scaling**, or **policy rollouts with feedback** to correct mistakes, refine strategy, and adapt to new scenarios over time (AgentGym‑RL 2025; UI‑Venus 2025).
* **Dense and Auxiliary Rewards**: A combination of dense rewards (feedback at each timestep) and auxiliary rewards (additional task-specific rewards, such as correct formatting or achieving sub-goals) accelerates learning and improves task performance, particularly in complex tasks. \cite{Agentgym-rl, 2025; rl-fine-tune-driving, 2024}

---

### 5. **Challenges and Future Directions**
**Description (Updated):**
This section addresses the ongoing challenges faced by AI‑driven companions, including issues related to **latency**, **safety**, and **out‑of‑distribution (OOD) behavior**. These challenges must be tackled to ensure that AI assistants can operate smoothly and safely in real‑time environments. We also explore **future directions** for improving system robustness and expanding AI capabilities in gaming and interactive systems.

**Actual Points:**

* **Latency and Real‑Time Performance**:
  AI companions must operate with **low latency** to ensure a smooth user (e.g., gaming) experience. Techniques such as **quantization**, **pruning**, and **on‑device processing** can help meet this need (UI‑Venus, 2025). Furthermore, real‑time systems in **interactive virtual environments** show that latency beyond ~100ms significantly affects user experience, requiring ultra‑low latency for a seamless response (Liu et al., 2023).
* **Safety and Robustness**:
  Handling **dangerous actions** and **critical errors** requires robust **confirmation mechanisms** and **rollback systems**. Ensuring that agents can **recover from errors** and avoid unintended actions is critical for maintaining safety, especially in complex tasks (OS‑Agents, 2024). Furthermore, ensuring **alignment** and **preventing unintended consequences** are important research areas to ensure safe interactions with AI‑driven assistants (Zubia et al., 2024).
* **Out-of-Distribution (OOD) Generalization**:
  Both V-Mage (2024) and Benchmarking-VLA-VLM (2025) identify OOD generalization as a critical failure point. V-Mage highlights that vision-only models struggle significantly to adapt to new visual scenarios. Similarly, Benchmarking-VLA-VLM found that all evaluated models (VLAs and VLMs) had "significant limitations in zero-shot generalization to OOD tasks," noting that the VLMs' performance was heavily influenced by factors like action representation and prompt engineering.
* **Future Directions**:
  Research should prioritize enhancing AI’s ability to handle complex, multi‑step tasks while ensuring **real‑time reliability** and **accuracy**. This requires enhancing **multi‑modal capabilities**, improving agent adaptability, and ensuring agents can generalize across environments (CRADLE, 2024). Moreover, increasing agent **resilience** to **unseen environments** (via proper safety and error recovery systems) and improving system **latency infrastructure** remain key challenges.

---

### 6. **Synthesis and Gaps in the Literature**

**Description (Updated):**
In this final part, we synthesize the key findings from previous sections and identify the **gaps** in existing research. Despite advancements in game companion systems, challenges remain in ensuring **contextual awareness**, **long-term interaction stability**, and **adaptability** to diverse game environments. This section sets the stage for the project by highlighting how it aims to fill these gaps.

**Actual Points:**

* **Gap in Relational AI and Context-Awareness:** While AI systems have shown progress in **task completion**, there is a significant lack of academic frameworks that effectively integrate **emotional intelligence** and **context-awareness** into long-term gaming interactions. Recent work, such as the **Emotion AWARE** framework (Gamage et al., 2024), highlights the complexity of this gap by demonstrating the need for multi-granular and explainable emotion modeling, a feature largely absent in current agent architectures.
* **Need for Unified Companion Systems:** This gap is evident in state-of-the-art academic solutions, which often lack the ability to provide **relational support** alongside functional task completion. Frameworks like **UI-Venus (2025)**, for example, have made significant strides in functional performance via structured actions but their architecture does not include or address the relational component. This project aims to fill this gap by creating a **companion-style assistant** that architecturally blends both companionship and agency.
* **Real-Time Adaptability:** Previous research has not fully addressed the **real-time adaptability** required for complex, dynamic games. This remains a recognized challenge, with benchmarks such as **lmgame-bench (2025)** being specifically designed to test and measure these capabilities. This project will focus on enhancing this aspect by leveraging **structured output** and **feedback-driven learning**.
* **Cross-Game Transferability:** Several studies, such as **CRADLE (2024)** and **ORAK (2025)**, have pointed out the difficulty of transferring models across different games, particularly when proprietary game APIs are involved. One key challenge in the literature is creating **game-agnostic agents** that can perform well in any environment without relying on specific game interfaces.


<!-- TODO: Note: The year number may be wrong. Need double check with Gemini, includes year, content validation (whether matches the citations) -->