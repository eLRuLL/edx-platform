"""
Python API for Demographics Status
"""

from openedx.features.enterprise_support.utils import is_enterprise_learner
from openedx.core.djangoapps.programs.utils import is_user_enrolled_in_program_type
from openedx.core.djangoapps.demographics.models import UserDemographics


def show_user_demographics(user, enrollments=None, entitlements=None):
    """
    Check if the user should be shown demographics collection fields. Currently limited
    to MicroBachlors Programs' learners who aren't part of an enterprise.
    """
    is_user_in_microbachelors_program = is_user_enrolled_in_program_type(
        user,
        "microbachelors",
        enrollments=enrollments,
        entitlements=entitlements
    )
    return is_user_in_microbachelors_program and not is_enterprise_learner(user)


def get_user_demographics_call_to_action_status(user):
    try:
        return UserDemographics.objects.get(user=user).call_to_action_dismissed
    except UserDemographics.DoesNotExist:
        return False
