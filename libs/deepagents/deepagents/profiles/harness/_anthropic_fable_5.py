"""Built-in Claude Fable 5 and Mythos 5 harness profiles.

Anthropic publishes one prompting guide for both models. This profile keeps
the shared Claude guidance and adds only supported steering for task scope,
evidence-backed progress, and completing autonomous work. Memory-system and
asynchronous-subagent recommendations are intentionally omitted because the
corresponding runtime capabilities are optional.

Scoped to the 5 generation on purpose. Fable 5.1 and Mythos 5.1 have distinct
model identifiers and their own prompting guide. Give 5.1 its own module
rather than widening these exact keys.

Source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5
"""

# ruff: noqa: E501
# Prompt sections are single lines by design so source wrapping does not
# alter the guidance injected into the system prompt.

from deepagents.profiles.harness._anthropic import (
    _claude_guidance_with_overlay,
)
from deepagents.profiles.harness.harness_profiles import (
    HarnessProfile,
    _register_harness_profile_impl,
)

_MODEL_SPECS: tuple[str, ...] = (
    "anthropic:claude-fable-5",
    "anthropic:claude-mythos-5",
)
"""Exact model specs sharing Anthropic's Fable 5 and Mythos 5 guidance.

Keep later generations such as Fable 5.1 and Mythos 5.1 in their own module
so their distinct prompting guidance does not inherit this overlay.
"""

_MODEL_SPECIFIC_OVERLAY = """\
<task_scope>
Do not add features, refactor, or introduce abstractions beyond what the task requires. Prefer the simplest complete solution for the stated requirements, and do not design for hypothetical future needs.
</task_scope>

<progress_grounding>
Before reporting progress, audit each claim against tool results from this session. Say explicitly when work is unverified, tests failed, or a step was skipped; state completed and verified outcomes plainly.
</progress_grounding>

<autonomous_completion>
Pause only for a destructive or irreversible action, a material scope change, or input only the user can provide. Otherwise, continue until the requested task is complete instead of ending with a promise or asking whether to proceed.
</autonomous_completion>"""
"""Claude Fable 5 and Mythos 5 guidance appended after the universal sections."""

_SYSTEM_PROMPT_SUFFIX = _claude_guidance_with_overlay(_MODEL_SPECIFIC_OVERLAY)
"""Text appended to the assembled base system prompt."""


def register() -> None:
    """Register the built-in Claude Fable 5 and Mythos 5 profiles."""
    profile = HarnessProfile(system_prompt_suffix=_SYSTEM_PROMPT_SUFFIX)
    for spec in _MODEL_SPECS:
        _register_harness_profile_impl(spec, profile)
