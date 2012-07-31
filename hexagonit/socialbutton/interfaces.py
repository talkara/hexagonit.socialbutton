from hexagonit.socialbutton import _
from hexagonit.socialbutton.vocabulary import social_button_code_ids
from plone.directives import form
from zope import schema
from zope.interface import Interface


class ISocialSiteRoot(Interface):
    """Site root marker."""


class ISocialCodesView(Interface):
    """SocialCodesView view"""

    def codes(*args, **kwargs):
        """Get social html codes"""


class IAddSocialButtonCode(form.Schema):

    code_id = schema.TextLine(
        title=_(u'ID'))

    code_text = schema.Text(
        title=_(u'Code'))

    code_icon = schema.TextLine(
        title=_(u'Icon'),
        required=False)


class ISocialButtonCode(IAddSocialButtonCode):

    code_id = schema.TextLine(
        title=_(u'ID'),
        readonly=True)


class IAddSocialButtonConfig(form.Schema):

    code_id = schema.Choice(
        title=_(u'ID'),
        source=social_button_code_ids)

    content_types = schema.Set(
        title=_(u'Content Types'),
        required=False,
        value_type=schema.Choice(
            vocabulary='plone.app.vocabularies.ReallyUserFriendlyTypes'))

    viewlet_manager = schema.Text(
        title=_(u'Viewlet Manager'),
        description=_(u'List names of viewlet manager line by line.'),
        default=u'plone.belowcontent')

    view_models = schema.Text(
        title=_(u'View Models'),
        description=_(u'List names of view model line by line.'),
        required=False,
        missing_value=u'')

    view_permission_only = schema.Bool(
        title=_(u'View permission only'),
        description=_(u'Display button only for views which has View permission.'),
        default=True)

    enabled = schema.Bool(
        title=_(u'Enabled'),
        default=True)


class ISocialButtonConfig(IAddSocialButtonConfig):

    code_id = schema.TextLine(
        title=_(u'ID'),
        readonly=True)


class ILanguageCountry(Interface):
    """Interface for language country mapping."""

    def __call__(lang, **kwargs):
        """Returns lang_country based on lang."""