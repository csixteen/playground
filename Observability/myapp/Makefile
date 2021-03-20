GO11MODULE=auto
GOFILES=$(wildcard *.go)

NAME=myapp

.PHONY: build
build: $(GOFILES) clean
	CGO_ENABLED=0 go build \
		-ldflags '-w -extldflags "-static"' \
		-gcflags "-trimpath $(GOPATH)/src"  \
		-o $(NAME)

.PHONY: clean
clean:
	go clean
	go mod tidy
	rm -f $(NAME)
