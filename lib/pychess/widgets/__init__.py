from gi.repository import Gtk

def insert_formatted(text_view, iter, text, tag=None):
    tb = text_view.get_buffer()
    # I know this is far from perfect but I don't want to use re for this
    if "://" in text or "www" in text:
        parts = text.split()
        for i, part in enumerate(parts):
            if "://" in part or "www" in part:
                parts[i] = '<a href="%s">%s</a>' % (part, part)
        label = Gtk.Label()
        label.set_markup(" ".join(parts))
        label.show()
        anchor = tb.create_child_anchor(iter)
        text_view.add_child_at_anchor(label, anchor)
    else:
        if tag is not None:
            tb.insert_with_tags_by_name(iter, text, tag)
        else:
            tb.insert(iter, text)
