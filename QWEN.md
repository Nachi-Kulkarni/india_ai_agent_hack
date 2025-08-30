# Qwen Code Context for India AI Agent Hackathon Project

## Project Overview

This repository contains the India AI Agent Hackathon project, focusing on building agentic AI applications using IBM's open-source technologies. The main project is "Kisan AI", an agricultural advisory system designed to assist Indian farmers through voice-based AI agents.

## Key Directories

- `kisan-ai/`: Main project directory for the agricultural advisory system
  - `config/`: Configuration files for the Kisan AI system
  - `docs/`: Documentation related to the implementation
  - `voice/`: Voice processing components, including integration with the Veena TTS model
- `.claude/`: Claude Code configuration and agent definitions
  - `agents/`: Specialized agent definitions for different tasks
  - `settings.json`: Claude Flow configuration settings
- `docs/`: General project documentation

## Project Type

This is a code project leveraging:
- IBM Watsonx Orchestrate ADK for agent orchestration
- Python for backend services
- Specialized AI models including the Veena TTS model for voice synthesis
- Claude Code framework for development workflows

## Key Technologies

1. **IBM Granite Models**: Foundation LLMs for agricultural, financial, and weather domains
2. **Watsonx Orchestrate ADK**: For building and orchestrating AI agents
3. **Veena TTS Model**: For ultra-realistic text-to-speech in Hindi and English
4. **Claude Code Framework**: Development methodology using SPARC principles

## Development Workflow

The project follows the SPARC methodology:
1. **Specification** - Requirements analysis
2. **Pseudocode** - Algorithm design
3. **Architecture** - System design
4. **Refinement** - Implementation with TDD
5. **Completion** - Integration and testing

Key development commands:
- `npx claude-flow sparc modes` - List available modes
- `npx claude-flow sparc run <mode> "<task>"` - Execute specific mode
- `npx claude-flow sparc tdd "<feature>"` - Run complete TDD workflow

## Kisan AI Project Structure

The Kisan AI system consists of multiple specialized agents:
- Crop Doctor Agent (plant health specialist)
- Climate & Weather Agent (hyperlocal weather predictions)
- Banking Consultant Agent (agricultural finance)
- Market Intelligence Agent (price tracking and profitability)
- Search & Knowledge Agent (agricultural information retrieval)
- WhatsApp Integration Agent (rich media sharing)

## Voice Interface

The system uses the Veena TTS model which provides:
- Sub-80ms latency
- 98% intelligibility
- Native Hindi-English code-mixing
- Multiple voice profiles

## Building and Running

To set up the development environment:
1. Install required dependencies (IBM Watsonx Orchestrate ADK)
2. Configure API keys for data sources (weather, market prices)
3. Set up the Veena TTS model integration

Key implementation phases:
1. Foundation setup (orchestration platform, core agents)
2. Knowledge base development
3. Real-time data integration
4. Advanced features (WhatsApp integration)
5. Optimization

## Development Conventions

- Follow SPARC methodology for all development tasks
- Use concurrent execution patterns (batch all related operations in a single message)
- Organize files in appropriate subdirectories (never save to root)
- Leverage the 54 available agents for specialized tasks
- Apply automated hooks for pre/post operation processing

## Key Files for Context

- `planning.md`: Detailed project planning and hackathon information
- `CLAUDE.md`: Claude Code configuration and development guidelines
- `.claude/settings.json`: Claude Flow settings and permissions
- `.claude/agents/base-template-generator.md`: Template generation agent definition