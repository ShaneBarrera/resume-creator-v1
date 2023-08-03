import requests
from bs4 import BeautifulSoup

def scrape_business_english_phrases(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-2xx status codes

        soup = BeautifulSoup(response.content, 'html.parser')
        h3_tags = soup.select('h3 a.tts-link')  # Find all the <a> tags with class "tts-link" inside <h3> tags

        phrases = []
        for a_tag in h3_tags:
            phrase = a_tag.get_text().strip()
            phrases.append(phrase)

        return phrases
    except requests.RequestException as e:
        print(f"Error during request: {e}")
        return None


word_list = [
    "watering", "cataloging", "hunting", "wanting", "holding", "taping", "integrating",
    "worrying", "loving", "spending", "fitting", "bating", "risking", "normalizing",
    "restructuring", "costing", "programming", "touching", "towing", "altering", "marketing",
    "yelling", "crushing", "beholding", "agreeing", "fencing", "sparkling", "wiping",
    "sparking", "slaying", "copying", "melting", "appraising", "complaining", "leading",
    "telling", "crashing", "subtracting", "normalizing", "grabbing", "wrecking", "thanking",
    "forming", "answering", "overhearing", "wriggling", "ringing", "admitting", "bruising",
    "making", "pumping", "melting", "bumping", "dragging", "consisting", "accepting",
    "dropping", "smelling", "recognizing", "facing", "deciding", "deserting", "riding",
    "ensuring", "frightening", "shading", "flapping", "washing", "completing", "heaping",
    "snoring", "draining", "clothing", "detailing", "initiating", "dispensing", "diagnosing",
    "paddling", "singing", "promising", "handling", "planing", "separating", "thriving",
    "shrinking", "scrubbing", "confusing", "spotting", "scattering", "noticing", "upgrading",
    "piloting", "estimating", "showing", "reigning", "folding", "contracting", "blushing",
    "broadcasting", "speaking", "slipping", "squashing", "pecking", "hanging", "returning",
    "receiving", "landing", "injecting", "fleeing", "cheering", "sniffing", "sleeping",
    "clinging", "breeding", "searching", "carving", "meaning", "attaching", "affording",
    "nesting", "undergoing", "passing", "entertaining", "longing", "enjoying", "fighting",
    "wrestling", "unfastening", "drawing", "supposing", "knotting", "greasing", "producing",
    "spinning", "squashing", "asking", "projecting", "enduring", "adopting", "fancying",
    "conducting", "conceiving", "guessing", "mating", "overthrowing", "regulating", "determining",
    "bearing", "devising", "abiding", "piloting", "hearing", "rhyming", "retrieving", "servicing",
    "integrating", "preaching", "rubbing", "clarifying", "agreeing", "striking", "wobbling",
    "groaning", "speeding", "filling", "repairing", "pining", "launching", "sneaking", "shaping",
    "breathing", "spoiling", "living", "recruiting", "proposing", "pedaling", "wrecking", "replacing",
    "operating", "trying", "licensing", "discovering", "overdoing", "rinsing", "camping", "displaying",
    "muddling", "pricking", "nesting", "processing", "counseling", "consolidating", "shivering",
    "numbering", "removing", "sliding", "referring", "ringing", "representing", "risking",
    "inspecting", "assisting", "enhancing", "administering", "identifying", "enacting", "skipping",
    "shaking", "spoiling", "spelling", "selecting", "shopping", "causing", "reflecting",
    "photographing", "withstanding", "evaluating", "breaking", "visiting", "creeping", "feeding",
    "loading", "graduating", "combing", "tickling", "catching", "dividing", "squealing",
    "breathing", "fixing", "floating", "logging", "chewing", "carrying", "hurting", "sacking",
    "expressing", "getting", "forbidding", "sawing", "moaning", "grinding", "ruining",
    "hurrying", "balancing", "exploding", "spilling", "welcoming", "eliminating", "acceding",
    "classifying", "smiling", "assuring", "settling", "scheduling", "perceiving", "moaning",
    "shooting", "reconciling"
]

word_list2 = [
    "watering", "cataloging", "hunting", "wanting", "holding", "taping", "integrating",
    "worrying", "loving", "spending", "fitting", "bating", "risking", "normalizing",
    "restructuring", "costing", "programming", "touching", "towing", "altering", "marketing",
    "yelling", "crushing", "beholding", "agreeing", "fencing", "sparkling", "wiping",
    "sparking", "slaying", "copying", "melting", "appraising", "complaining", "leading",
    "telling", "crashing", "subtracting", "normalizing", "grabbing", "wrecking", "thanking",
    "forming", "answering", "overhearing", "wriggling", "ringing", "admitting", "bruising",
    "making", "pumping", "melting", "bumping", "dragging", "consisting", "accepting",
    "dropping", "smelling", "recognizing", "facing", "deciding", "deserting", "riding",
    "ensuring", "frightening", "shading", "flapping", "washing", "completing", "heaping",
    "snoring", "draining", "clothing", "detailing", "initiating", "dispensing", "diagnosing",
    "paddling", "singing", "promising", "handling", "planing", "separating", "thriving",
    "shrinking", "scrubbing", "confusing", "spotting", "scattering", "noticing", "upgrading",
    "piloting", "estimating", "showing", "reigning", "folding", "contracting", "blushing",
    "broadcasting", "speaking", "slipping", "squashing", "pecking", "hanging", "returning",
    "receiving", "landing", "injecting", "fleeing", "cheering", "sniffing", "sleeping",
    "clinging", "breeding", "searching", "carving", "meaning", "attaching", "affording",
    "nesting", "undergoing", "passing", "entertaining", "longing", "enjoying", "fighting",
    "wrestling", "unfastening", "drawing", "supposing", "knotting", "greasing", "producing",
    "spinning", "squashing", "asking", "projecting", "enduring", "adopting", "fancying",
    "conducting", "conceiving", "guessing", "mating", "overthrowing", "regulating", "determining",
    "bearing", "devising", "abiding", "piloting", "hearing", "rhyming", "retrieving", "servicing",
    "integrating", "preaching", "rubbing", "clarifying", "agreeing", "striking", "wobbling",
    "groaning", "speeding", "filling", "repairing", "pining", "launching", "sneaking", "shaping",
    "breathing", "spoiling", "living", "recruiting", "proposing", "pedaling", "wrecking", "replacing",
    "operating", "trying", "licensing", "discovering", "overdoing", "rinsing", "camping", "displaying",
    "muddling", "pricking", "nesting", "processing", "counseling", "consolidating", "shivering",
    "numbering", "removing", "sliding", "referring", "ringing", "representing", "risking",
    "inspecting", "assisting", "enhancing", "administering", "identifying", "enacting", "skipping",
    "shaking", "spoiling", "spelling", "selecting", "shopping", "causing", "reflecting",
    "photographing", "withstanding", "evaluating", "breaking", "visiting", "creeping", "feeding",
    "loading", "graduating", "combing", "tickling", "catching", "dividing", "squealing",
    "breathing", "fixing", "floating", "logging", "chewing", "carrying", "hurting", "sacking",
    "expressing", "getting", "forbidding", "sawing", "moaning", "grinding", "ruining",
    "hurrying", "balancing", "exploding", "spilling", "welcoming", "eliminating", "acceding",
    "classifying", "smiling", "assuring", "settling", "scheduling", "perceiving", "moaning",
    "shooting", "reconciling", "faxing", "executing", "decaying", "marrying", "stinging",
    "investigating", "enacting", "caring", "questioning", "proving", "rescuing", "filming",
    "shopping", "separating", "identifying", "leading", "laying", "speeding", "tracing",
    "identifying", "alerting", "sacking", "remaining", "activating", "interesting", "boasting",
    "imagining", "putting", "controlling", "disliking", "addressing", "solving", "fleeing",
    "agreeing", "shining", "fancying", "wringing", "fading", "accelerating", "establishing",
    "curling", "attacking", "guaranteeing", "deceiving", "patting", "applauding", "noting",
    "pressing", "kneeling", "hitting", "scheduling", "presiding", "repeating", "prescribing",
    "arising", "slaying", "adding", "fitting", "snoring", "shaking", "sewing", "inspecting",
    "educating", "manipulating", "belonging", "giving", "participating", "agreeing", "doubting",
    "misunderstanding", "following", "trotting", "writing", "clinging", "interesting", "damming",
    "correlating", "plugging", "attending", "retiring", "beholding", "understanding", "walking",
    "pinpointing", "photographing", "braking", "soaking", "folding", "remembering", "slinging",
    "borrowing", "rocking", "allowing", "filming", "obeying", "coiling", "cycling"
]


if __name__ == "__main__":
    url = "https://www.fluentu.com/blog/business-english/how-to-speak-business-english/"
    phrases = scrape_business_english_phrases(url)
    if phrases:
        for phrase in phrases:
            print(phrase)

