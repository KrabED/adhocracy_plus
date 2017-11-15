from pytest_factoryboy import register

from adhocracy4.test import factories as a4_factories
from adhocracy4.test.factories.maps import AreaSettingsFactory
from adhocracy4.test.helpers import patch_background_task_decorator
from liqd_product.apps.django_overwrites.urlresolvers import patch_reverse
from meinberlin.test import factories as mb_factories

from . import factories
from .partners import factories as partner_factories


def pytest_configure(config):
    # Patch the reverse function.
    # This is required as modules are imported by pytest prior to app init
    patch_reverse()
    # Patch email background_task decorators for all tests
    patch_background_task_decorator('adhocracy4.emails.tasks')


register(factories.UserFactory)
register(factories.UserFactory, 'user2')
register(factories.AdminFactory, 'admin')
register(factories.OrganisationFactory)
register(partner_factories.PartnerFactory)

register(mb_factories.PhaseFactory)
register(mb_factories.PhaseContentFactory)
register(mb_factories.CategoryFactory)

register(a4_factories.ProjectFactory)
register(a4_factories.ModuleFactory)
register(AreaSettingsFactory)
