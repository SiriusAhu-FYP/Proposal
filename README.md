# FYP Proposal (DDL: 2025-11-21)

This README.md is to help me to clearly organize and manage the contents of my FYP proposal, and also to contribute to the future dissertation writing.

## About the Contents

**Based on the FYP proposal template provided by school**, we should have 4 main sections.

And here I record **my understanding** of each section and subsections. (How will I write them? What to include?)

### 1. Introduction

#### 1.1 Problem Statement & Motivation

- Point out the demand for **interactive and companion-like experiences** for entertainment is shifting: **from simple automation / static overlays -> genuine engagement & companionship**.

- Overview of such demand is attracting people's attention:
  - a) Game aspects: Both single games like `AI2U` (\cite{ai2u_game}) and big companies like `NVIDA` and `Ubisoft` are focusing on building interactive NPCs to enhance user experience (\cite{nvidia_ace_autonomous_2025, ubisoft_neo_npc_2024}).
    - Evidence of AI contributes to actual market value \cite{inworld_market_validation_2023}
  - b) Streaming aspects: The success of AI-driven virtual streamer `Neuro-sama` demonstrates a growing market (\cite{neurosama_youtube, streamelements_state_2024, streamscharts_q4_2024_landscape}), plus it inspires a vibrant open-source ecosystem (\cite{open_llm_vtuber, airi_project, kimjammer_neuro}).
    - A commercial evidence: \cite{neurosama_hype_streamscharts_2025}
  - i.e. support such demand by market and tech community evidence.

- Outline this project is timely (<span style="color:red">Consider whether to remove this paragraph</span>)
  - **Unified evaluation protocols & Modular ablation frameworks** provided by \cite{ORAK, lmgame-bench}
- **GCC availability** proved by \cite{CRADLE, ui-venus}

- Brief introduction to my project (<span style="color:red">Consider to improve it after finishing other parts</span>)

#### 1.2 Key Challenges

- List some main challenges and possible solutions found from the literature review.

#### 1.3 Scope, Objectives and Deliverables
##### Scope
> How I'll approach the problem, and what will **not** be done.
1. `Unified Action Interface via GUI (GCC)`: A human-homorphic channel with "screen in, keyboard/mouse out" paradigm, which can avoid the dependency on game-specific APIs. (proved feasible by `\cite{CRADLE, ui-venus, Benchmarking-VLA-VLM}`)
2. `Structured Output with Constrained Action Selection`: a) The output of LLM is restricted to a pre-defined format, such as some specified JSON schema; b) To mitigate the hallucination issue, the action space is constrained to a pre-defined set of general actions (e.g., "move forward", "open inventory", etc.)
3. `Low-Coupling Orchestration`: Use MCP-style orchestration to implement "plug-and-play" modules, which can facilitate future extensions and ablation studies.

**Out-of-Scope**:
1. (Re-claim) No application/game-specific APIs will be involved.
2. No large-scale end-to-end training or data collection will be conducted.
3. Though **VLA** models seem to be more suitable to generate actions based on visual input, they're not designed as a part of this project's focus, thus some related work will just be used as a benchmark comparison (\cite{Benchmarking-VLA-VLM}) if possible.
4. Some works utilize A11y/private DOM hooks as a benchmark. We may do a comparison with these methods if time permits, but our pipeline doesn't include these components.

##### Objectives
Develop a GCC-based prototype:
  - a) Core functions: Event spotting + Tactical guidance + Voice Loop
  - b) Use MCP-style orchestration to implement "plug-and-play" modules
    - with at least these 4 core modules: skills, planning, memory and reflection

Define some metrics to measure the performance of the prototype
  - e.g., pass@k (pass at k-th attempt), Invalid% (Timesteps with invalid preds / Total number of timesteps) \cite{Benchmarking-VLA-VLM} ⚠️ Many metrics available here

##### Deliverables
1. A system protype, featuring agentic modules, a GUI executor, and safety guards.
2. Evaluation scripts
3. User docs and demos (videos)

<div style="color:red">Mix Objectives and Deliverables?</div>

#### 1.4 Design Principles & System Preview

<div style="color:red">Put to Section 3. Project Plan, or just remove?</div>

**Principles**:
1. `Unified Input`
2. `Structured Output with Constrained Action Selection`
3. `Low-Coupling Orchestration`

**System Preview**:
Explain how the system works. (maybe with a diagram)

#### 1.5 Glossary Alignment
1. GCC: General Computer Control, a human-homorphic
2. Skill: The skill / tool set that an agent can use. Also named macro in some literatures.
...

<div style="color:red">BTW: Is "Related Work" necessary in proposal?</div>

### 2. Literature Review

### 3. Project Plan

### 4. Conclusion