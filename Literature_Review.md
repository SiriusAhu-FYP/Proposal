### 1. **Feasibility of Human-Homomorphic Interfaces (GUI/GCC)**

**Description (Updated)**:
This section discusses the use of **human-homomorphic interfaces (GUI/GCC)** for achieving cross-platform compatibility, eliminating the need for game-specific APIs. The focus is on demonstrating how GUI-based interaction can create adaptable, dynamic AI systems that can seamlessly integrate into different games and platforms. These approaches are grounded in **legal move constraints**, **action representation formats**, and **state representation**, ensuring stability across different gaming environments. This enables a consistent user experience without the reliance on proprietary game APIs.

**Actual Points**:

* **General Computer Control (GCC)**: The feasibility of a game-agnostic interface is demonstrated by the `CRADLE` framework. It introduces the "Screen as input, keyboard/mouse as output" (GCC) paradigm, proving that a unified agent can perform complex, long-horizon tasks across different software (including games) without relying on specialized APIs. \cite{CRADLE}
* **Structured Action Feasibility**: The `UI-Venus` framework, inspired by DeepSeek-R1 and using Reinforcement Fine-Tuning (RFT), further validates the "Screenshot $\rightarrow$ Structured Action" pipeline. It demonstrates the feasibility of this approach by training a model on GUI tasks, reinforcing that GUI-based control is a viable and powerful paradigm. \cite{ui-venus, ponder-press}
* **Hierarchical Planning and Memory**: The `Agent S` framework provides another strong validation of the GCC paradigm for complex tasks. Its key contribution is "Experience-Augmented Hierarchical Planning," where the agent learns from both external knowledge and its own internal "narrative" and "episodic" memory to decompose and solve long-horizon goals. \cite{AgentS}
* **Legal Move Constraints**: The `ORAK` benchmark highlights the importance of using a restricted valid-action set, or **Legal Move Constraints**. This feature, which greatly constrains the output space of the model, is a critical optimization that can reduce action errors by 15-20%. \cite{ORAK}
* **Move Representation Format**: Action representation is a non-trivial challenge, as noted in the `ORAK` benchmark \cite{ORAK}. The `CodeAct` framework proposes a powerful solution by using **executable Python code** as the agent's output. This is more robust than static JSON, as it can handle complex logic (loops, variables) and allows the agent to **self-debug** by receiving and correcting its own error tracebacks. \cite{CodeAct}
* **State Representation**: The `ORAK` benchmark also introduces a standardized **State Representation Format** (e.g., agent position, task progress), which provides richer context for the agent and is essential for cross-game generalization. \cite{ORAK}
* **Input Modality**: `ORAK` is explicitly designed to evaluate agents using three different input modes: **Text-only**, **Image-only**, and **Text + Image**, allowing for a direct comparison of perceptual models. \cite{ORAK}
* **Multi-modal Inputs**: `V-MAGE` demonstrates that **vision-only inputs** pose significant generalization challenges \cite{v-mage}, while `Ponder & Press` supports a vision-only (no DOM/HTML) approach for improving generalizability across platforms. \cite{ponder-press}
---

### 2. **Evaluation Protocols & Performance Metrics**

**Description (Updated)**:
This section covers the evaluation frameworks used to measure the performance of AI assistants in dynamic gaming environments. By analyzing metrics such as **pass@k**, **Invalid%**, and **Opportunity-Normalized Success (OAS)**, we can evaluate the AI's effectiveness, efficiency, and error rate. These metrics also guide the design of **scaffolding** and **feedback mechanisms** that enhance AI stability and reliability over time. Proper benchmarking and **task-specific performance metrics** are essential for evaluating AI systems in real-world gaming scenarios.

**Actual Points**:

* **pass@k**: Measures how many attempts an AI needs to successfully complete a task. This metric is commonly used in decision‑making tasks to track success across multiple attempts and is particularly useful for evaluating task performance over repeated trials.
* **Invalid%**: Tracks the proportion of **invalid actions** taken by the AI. A high `Invalid%` indicates the model struggles to produce valid outputs, a key metric identified in benchmark surveys. \cite{Benchmarking-VLA-VLM, gui-agents-survey}
* **Granular Skill Assessment**: The `V-Mage` framework provides a granular assessment of MLLM failures via **"Unit Tests for Core Visual Abilities,"** identifying specific failure modes in positioning, direction, identification (e.g., seeing paths as obstacles), and a "fight" between correct reasoning and incorrect execution. \cite{v-mage}
* **Benchmarking and Task-Specific Metrics**: Systems like **ORAK** and **lmgame-bench** provide comprehensive frameworks for systematically evaluating AI performance across multiple game types and specific tasks. \cite{lmgame-bench, ORAK}
* **Dynamic ELO System**: `V-Mage` introduces a **Dynamic ELO system** to address cross-game comparison, helping standardize agent performance across different games. \cite{v-mage}
* **Reward Structures**: To properly evaluate agents on long-horizon tasks, benchmarks like `ORAK` employ a mix of reward types, including **Dense Rewards** (continuous feedback) and **Auxiliary Rewards** (e.g., for "correct format output"). \cite{ORAK}
* **OOD Generalization Findings**: A primary outcome from benchmarks is the poor performance of current models on out-of-distribution (OOD) tasks, identified as a major unsolved challenge. \cite{Benchmarking-VLA-VLM, v-mage, VisualAgentBench, gui-agents-survey}
* **Human-Centered Metrics**: Recent position papers argue for a **"Human-Centered Evaluation Framework,"** stating that metrics must also include **latency, safety, privacy, robustness, and error-recovery mechanisms** (like rollbacks). \cite{human-centered-eval}


---

### 3. **Agentic Modules and Stability in Long-Horizon Tasks**

**Description (Updated)**:
This part explores the **agentic modules** (planning, memory, reflection, skills) that help maintain long-term stability in AI companions. These modules are critical in mitigating **error accumulation** and ensuring the AI can function reliably over extended tasks. By combining these modules, the system can handle **complex, long-sequence decision-making**, providing a robust AI assistant that supports players through sustained gameplay without drifting off course.

**Actual Points**:

* **Modular Orchestration (AgentOrchestra)**: The core architecture will be a hierarchical multi-agent framework, as proposed by `AgentOrchestra`. This "conductor" model features a central "planning agent" that decomposes complex objectives and delegates sub-tasks to "specialized agents" (e.g., a functional agent, a relational agent, a knowledge agent). This approach provides a clear implementation of **task segmentation**, allowing long-horizon tasks to be broken down and managed by feedback loops. \cite{AgentOrchestra, Multi-Agent-Collab-Survey, os-agents, CRADLE}
* **Orchestration Protocol (MCP)**: For the "plug-and-play" `AgentOrchestra` architecture to function, a standardized "Model Context Protocol" (MCP) is necessary. This is the "missing puzzle piece" that `ORAK` and other frameworks use to allow the central conductor to "seamlessly interact" with the specialized agentic modules. \cite{ORAK, MCP-Huggingface}
* **Planning and Reflection**: The "conductor" agent's internal logic will be an \textbf{agentic chain}, as demonstrated in the `CRADLE` framework, which includes modules for "Info Gathering," "Self-Reflection," "Skill Curation," and "Action Planning." This aligns with surveys like `OS-Agents`, which also identify adaptive planning based on environmental feedback as a cornerstone of modern agent design. \cite{CRADLE, os-agents}
* **Memory**: Memory is a critical module for long-horizon planning. The `Agent S` framework provides a powerful model for this, using "Experience-Augmented Hierarchical Planning" that retrieves from long-term "narrative memory" (past tasks) and "episodic memory" (past steps). This is a more advanced implementation of the "memory scaffolding" concept seen in `lmgame-bench` and the "action recording" specified by `OS-Agents`. \cite{AgentS, lmgame-bench, os-agents, ORAK}
* **Error Mitigation (BacktrackAgent)**: To prevent error accumulation and **task drift**, a dedicated safety module based on the `BacktrackAgent` framework is required. This module uses a "Verifier" (for simple failures, e.g., no screen change), a "Judger" (to identify semantic errors, e.g., "Game Over" screen), and a "Reflector" (to backtrack to a known good state and replan). This is a robust implementation of the simple feedback loop mentioned by `OS-Agents`. \cite{BacktrackAgent, lmgame-bench, os-agents}
* **Skill Curation**: A modular approach to task-solving that involves breaking down actions into atomic skills. This concept is widely adopted, with surveys like `Agent-AI` identifying "Macros (or skills)" as a common feature. The `CRADLE` framework implements this directly with its "Skill Curation" module, which dynamically generates and updates re-usable skills to handle complex, long-term tasks. \cite{CRADLE, agent-ai}
* **Self-Evolution**: A key new direction for agents is **Self-Evolution**, or the ability to automatically assemble new skill-sets for novel tasks. The `UI-Venus` report provides a practical implementation of this, with a "Self-Evolving Trajectory History Alignment" framework. This method acts as automated reflection, allowing the agent to re-evaluate its past actions, filter for successful "thought-action pairs," and refine its own reasoning, leading to "more coherent planning." \cite{ui-venus, llm-ga}
---

### 4. **Learning Paradigms for Robust Agent Training**

**Description (Updated)**:
This section presents the major learning paradigms that underpin the training of interactive game/GUI assistants. In particular, it emphasizes how **reinforcement‑fine‑tuning (RL‑finetune)**, **structured action generation**, and **iterative feedback/refinement loops** enable agents to learn in long‑horizon, dynamic environments, bridging the gap between single‑step action models and sustained interactive assistance.

**Actual Points**:

* **RL‑Finetuning (RFT)**: RFT is a key paradigm for training specialized GUI agents. The `UI-AGILE` framework provides a SOTA training methodology, proposing novel reward-shaping techniques like a "Continuous Grounding Reward" (to incentivize precision) and a "Simple Thinking" Reward (to balance speed and reasoning). \cite{UI-AGILE, ui-venus, agent-gym-rl}
* **Structured Action Generation (CodeAct)**: To ensure reliability, the agent's output must be structured. The `CodeAct` framework proposes a highly robust method: using **executable Python code** as the action output. This allows the agent to **self-debug** by receiving an error traceback from the interpreter and correcting its own code, a process not possible with static JSON or discrete macro actions. \cite{CodeAct, We-Need-Structured-Output, ui-venus}
* **Iterative Feedback/Refinement Loops**: Agents employ mechanisms such as **self‑evolving trajectories** (`UI-Venus`) or **progressive interaction scaling** (`AgentGym-RL`) or **policy rollouts with feedback** to correct mistakes, refine strategy, and adapt to new scenarios over time. \cite{agent-gym-rl, ui-venus}
* **Dense and Auxiliary Rewards**: A combination of **dense rewards** (feedback at each timestep) and **auxiliary rewards** (additional task-specific rewards, such as correct formatting or achieving sub-goals) accelerates learning and improves task performance, particularly in complex tasks. \cite{agent-gym-rl, rl-fine-tune-driving}
* **Offline Learning (Decision Transformers)**: As an alternative to online RFT, offline learning paradigms like the `Decision Transformer` (DT) frame RL as a sequence modeling problem, allowing agents to learn from static datasets of expert behavior, as explored by frameworks like `R2-Play`. \cite{Decision-Transformer, r2-play}
* **Grounded Task Execution**: To improve reliability and reduce errors, agent training also focuses on **"Grounded" task execution**. This involves explicitly tying an agent's actions to the context of the UI or game state (e.g., "right-click 'Context'"), which helps to reduce ambiguity and prevent the model from "drifting" or hallucinating invalid actions. \cite{agent-ai}
* **Hybrid Offline Generation (PORTAL)**: A key paradigm for solving latency is proposed by the `PORTAL` framework. It uses the LLM *offline* to generate a game-playing policy as a **Behavior Tree (BT)**. The runtime agent is a simple, non-neural interpreter that executes this compiled BT, achieving **zero-latency** execution. \cite{PORTAL}
---

### 5. **Challenges and Future Directions**
**Description (Updated):**
This section addresses the ongoing challenges faced by AI‑driven companions, including issues related to **latency**, **safety**, and **out‑of‑distribution (OOD) behavior**. These challenges must be tackled to ensure that AI assistants can operate smoothly and safely in real‑time environments. We also explore **future directions** for improving system robustness and expanding AI capabilities in gaming and interactive systems.

**Actual Points:**

* **Latency and Real‑Time Performance**: AI companions must operate with **low latency** to ensure a smooth user (e.g., gaming) experience, as real‑time systems in interactive virtual environments show that latency beyond ~100ms significantly affects user experience \cite{liu2023llm}. [cite_start]This is a critical challenge, with the **PORTAL** framework proposed as a "zero-latency" solution by compiling LLM policies into Behavior Trees [cite: 2511-2514], and the `Human-Centered Evaluation` framework identifying it as a critical metric. \cite{human-centered-eval, ui-venus}
* **Safety and Robustness**: Handling **dangerous actions** and **critical errors** requires robust safety systems, including confirmation mechanisms and rollback systems, to ensure agents can recover from errors and avoid unintended consequences \cite{os-agents, zubia2024robustifying, human-centered-eval}. The **BacktrackAgent** framework provides a concrete solution, with a 3-module architecture ("Verifier," "Judger," "Reflector") to detect, assess, and recover from semantic errors (e.g., "Game Over" screen). \cite{BacktrackAgent}
* **Out-of-Distribution (OOD) Generalization**: OOD generalization is a critical failure point for most agents \cite{v-mage, Benchmarking-VLA-VLM, VisualAgentBench}. The **PORTAL** framework offers a breakthrough solution, demonstrating unprecedented cross-game generalization by compiling policies that were successfully applied to thousands of different 3D games. \cite{PORTAL}
* **Long-Horizon & Fine-Grained Failures**: Recent surveys identify that current agents, while proficient in simple tasks, still struggle with two key failures. First, **long-horizon tasks easily fail** as errors accumulate over time. Second, agents have **low fine-grainedness or resolution**, making it difficult to perform precise actions (e.g., drag-and-drop, pixel-level clicks). \cite{mllm-gui, os-agents, gui-agents-survey}
* **Future Directions**: Research should prioritize enhancing AI’s ability to handle complex, multi‑step tasks while ensuring **real‑time reliability** and **accuracy**. This requires enhancing **multi‑modal capabilities**, improving agent adaptability, and increasing agent **resilience** to unseen environments, as noted by the `CRADLE` framework and the need for robust error recovery and latency solutions. \cite{CRADLE, BacktrackAgent, PORTAL}

---

### 6. **Synthesis and Gaps in the Literature**

**Description (Updated):**
In this final part, we synthesize the key findings from previous sections and identify the **gaps** in existing research. Despite advancements in game companion systems, challenges remain in ensuring **contextual awareness**, **long-term interaction stability**, and **adaptability** to diverse game environments. This section sets the stage for the project by highlighting how it aims to fill these gaps.

**Actual Points:**

* **Gap in Relational AI and Context-Awareness**: The primary literature gap is identified by the **Four-Quadrant Taxonomy** (Sun & Wu, 2025), which separates AI companions on an **(Emotional vs. Functional)** axis. Current research is bifurcated, leaving the blend of these quadrants as a key gap, with frameworks like `EmotionAWARE` highlighting the complexity of the "Emotional" component. \cite{Four-Quadrant-Taxonomy, EmotionAWARE}
* **Need for Unified Companion Systems**: This gap is evident in SOTA functional architectures like `AgentOrchestra` and `UI-Venus`, which are exclusively focused on task completion (the "Functional" axis) and do not include or address the relational component. \cite{AgentOrchestra, ui-venus}
* **Justification for Unification**: The HCI study, **"Cooperation Between Player and AI"** (Braun et al., 2024), provides the core justification for this project. It found that a **strong functional agent is a prerequisite for a good relational bond**, as players reject "dumb" companions that increase their workload. This proves the hypothesis that function and relation must be unified. \cite{Cooperation-Player-AI}
* **Real-Time Adaptability Gap**: Previous research has not fully addressed the **real-time adaptability** required for complex, dynamic games, a challenge that benchmarks like `lmgame-bench` are specifically designed to test. \cite{lmgame-bench}
* **Cross-Game Transferability Gap**: Creating **game-agnostic agents** is a key challenge, as noted by `CRADLE` and `ORAK` \cite{CRADLE, ORAK}. The **PORTAL** framework's success in this area highlights it as a critical SOTA research direction. \cite{PORTAL}

<!-- TODO: Note: The year number may be wrong. Need double check with Gemini, includes year, content validation (whether matches the citations) -->