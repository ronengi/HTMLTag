#!/usr/bin/python


class HTMLTag:
    """Performs various actions related to html tags.

    generate()  create html tag from dictionary object.
    """

    @staticmethod
    def get_info(info=None, taglines=[]):
        # print(info)
        if info.__class__.__name__ in ('dict'):
            for key, val in info.items():
                # todo: future key could be a tuple
                if key in ('html', 'body', 'div', 'span', 'p'):
                    taglines.append('<{0}'.format(key))
                    HTMLTag.get_info(val, taglines)
                    taglines.append('</{0}>'.format(key))
                elif key in ('t_id'):
                    # val must be str
                    taglines.append('id="{0}"'.format(val))
                elif key in ('t_classes'):
                    # val must be sub-list
                    classlines = ['class="']
                    for item in val:
                        classlines.append('{0} '.format(item))
                    classlines.append('"')
                    taglines.append(''.join(classlines))
                elif key in ('t_styles'):
                    # val must be sub-dictionary
                    stylelines = ['style="']
                    for subkey, subval in val.items():
                        stylelines.append('{0}: {1}; '.format(subkey, subval))
                    stylelines.append('"')
                    taglines.append(''.join(stylelines))
                elif key in ('left', 'top', 'right', 'bottom', 'width', 'height'):
                    taglines.append('{0}: {1};'.format(key, val))
                elif key in ('t_properties'):
                    # val must be sub-dictionary
                    for subkey, subval in val.items():
                        taglines.append('{0}="{1}"'.format(subkey, subval))
                elif key in ('t_contents'):
                    taglines.append('>')
                    # val must be a list
                    for item in val:
                        HTMLTag.get_info(item, taglines)
                else:
                    taglines.append('{0}:'.format(str(key)))
                    HTMLTag.get_info(val, taglines)
                    taglines.append('/{0}'.format(str(key)))

        elif info.__class__.__name__ in ('list'):
            for item in info:
                HTMLTag.get_info(item, taglines)
        else:
            taglines.append('{0}'.format(str(info)))

    @staticmethod
    def generate(info: dict = {}) -> str:
        """Generate html code for tag creation.

        :return: string of html tag ready to display.
        :argument info: dictionary with all necessary tag data
                        t_type:         the html tag type
                        t_id            the tag id
                        t_classes       list of all tag classes
                        t_styles        list of all inline style details
                        t_properties    additional tag properties
                        t_contents      the text inside the tag
        """

        taglines = []
        HTMLTag.get_info(info, taglines)
        # print(info, '<br>\n')
        # for item in taglines:
        #     print('{0}<br>\n'.format(item))
        return ' '.join(taglines)

