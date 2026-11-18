# Build the EPEC 2026 talk into build/
#   make        -> build/slides.pdf (two pdflatex passes for page totals)
#   make clean  -> remove LaTeX auxiliary files, keep the PDF
#   make purge  -> remove the whole build/ folder

MAIN     := slides
BUILD    := build
LATEX    := pdflatex
FLAGS    := -interaction=nonstopmode -halt-on-error -output-directory=$(BUILD)

PDF      := $(BUILD)/$(MAIN).pdf
DEPS     := $(MAIN).tex $(wildcard figs/*) $(wildcard logo/*)

.PHONY: all clean purge

all: $(PDF)

$(PDF): $(DEPS) | $(BUILD)
	$(LATEX) $(FLAGS) $(MAIN).tex > /dev/null || (grep -A5 '^!' $(BUILD)/$(MAIN).log; exit 1)
	$(LATEX) $(FLAGS) $(MAIN).tex > /dev/null || (grep -A5 '^!' $(BUILD)/$(MAIN).log; exit 1)
	@echo "Built $(PDF)"

$(BUILD):
	mkdir -p $(BUILD)

clean:
	rm -f $(addprefix $(BUILD)/$(MAIN).,aux log nav out snm toc vrb)

purge:
	rm -rf $(BUILD)
