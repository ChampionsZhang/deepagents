"""Built-in Claude Opus 4.7 harness profile.

Layers a system-prompt suffix onto `anthropic:claude-opus-4-7` tuned to
Claude Opus 4.7's documented behaviors:

- Universal Claude guidance that applies to every recent Claude —
  parallel tool calls, grounded (non-speculative) answers, and
  post-tool-result reflection.
- Claude Opus 4.7-specific overlays that counter the model's documented
  tendency to use tools and spawn subagents less aggressively than
  prior Opus generations when not prompted otherwise.

Source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
"""

# ruff: noqa: E501
# Prompt sections are single lines by design to match Anthropic's
# published samples verbatim; hard-wrapping them would diverge from the
# source of truth and make future updates harder to diff.

from deepagents.profiles.harness._anthropic import (
    _claude_guidance_with_overlay,
)
from deepagents.profiles.harness.harness_profiles import (
    HarnessProfile,
    _register_harness_profile_impl,
)

_MODEL_SPECIFIC_OVERLAY = """\
<tool_usage>
When a task depends on the state of files, tests, or system output, use tools to observe that state directly rather than reasoning from memory about what it probably contains. Read files before describing them. Run tests before claiming they pass. Search the codebase before asserting a symbol does or does not exist. Active investigation with tools is the default mode of working, not a fallback.
</tool_usage>

<subagent_usage>
Do not spawn a subagent for work you can complete directly in a single response (e.g. refactoring a function you can already see).

Spawn multiple subagents in the same turn when fanning out across items or reading multiple files.
</subagent_usage>"""
"""Claude Opus 4.7-specific guidance appended after the universal sections."""

_SYSTEM_PROMPT_SUFFIX = _claude_guidance_with_overlay(_MODEL_SPECIFIC_OVERLAY)
"""Text appended to the assembled base system prompt."""


def register() -> None:
    """Register the built-in Claude Opus 4.7 harness profile."""
    _register_harness_profile_impl(
        "anthropic:claude-opus-4-7",
        HarnessProfile(system_prompt_suffix=_SYSTEM_PROMPT_SUFFIX),
    )
