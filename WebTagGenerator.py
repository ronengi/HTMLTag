#!/usr/bin/python


# todo: implement a separate <div> creator
# todo: after that implement a general <tag> creator

class WebTagGenerator:
    """Generate html code for tag creation.
    
    info:   dictionary with all necessary tag data
            t_type:         the html tag type
            t_id            the tag id
            t_classes       list of all tag classes
            t_styles        list of all inline style details
            t_properties    additional tag properties
            t_contents      the text inside the tag
    
    """

    @staticmethod
    def generate_html(info={}):
        tag = {'t_id': self.__infotom.get_it_id()
            , 't_classes': []
            , 't_styles': []
            , 't_properties': []
            , 't_contents': []}

        if it.get_lang_rtl():
            html_div['classes'].append('lang_rtl')

        html_div['styles'].append('left: {0}px;'.format(str(it.get_left())))
        html_div['styles'].append('top: {0}px;'.format(str(it.get_top())))
        html_div['styles'].append('width: {0}px;'.format(str(it.get_width())))
        html_div['styles'].append('height: {0}px;'.format(str(it.get_height())))

        if isinstance(it, InfoTom):
            html_div['classes'].append('InfoTom')
            html_div['properties'].append('draggable="true"')
            html_div['contents'].append(str(it))
            html_div['contents'].append(WebInfoTom.add_resize_handle(it_id=html_div['it_id']))

        tag = '<{0} id="{1}" class="{2}" style="{3}" {4}>{5}</{0}>'.format(
            info['t_type']
            , info['t_id']
            , ' '.join(info['t_classes'])
            , ' '.join(info['t_styles'])
            , ' '.join(info['t_properties'])
            , '\n'.join(info['t_contents']))

        return tag



tag = dict(
    t_type='div'
    , t_id='it_id_1'
    , t_classes=['class1', 'class2', 'class3']
    , t_styles={'left': '12px', 'top': '13px'}
    , t_properties={'draggable': 'true'}
    , t_contents='the text inside the tag')

print(WebTagGenerator.generate_html(tag))

