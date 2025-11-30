
def generate_for_campaign(campaign_name, sample_messages, common_words, n=5):
    templates = [
        "{hook} — {benefit}. {cta}",
        "Limited time: {hook}. {benefit}. {cta}",
        "{hook} + {cta}",
    ]
    ctas = ["Shop now","Buy now","Learn more","Get yours","Limited offer"]
    benefits = ["all-day comfort","perfect fit","premium quality","best value","wire-free support"]
    hooks = [w.title() for w in (common_words[:5] + ["Feel confident","Invisible support","Perfect fit"])]
    out = []
    for i in range(n):
        t = templates[i % len(templates)]
        out.append({'headline': t.format(hook=hooks[i%len(hooks)], benefit=benefits[i%len(benefits)], cta=ctas[i%len(ctas)]),
                    'rationale':'Derived from common words and benefit templates'})
    return out
