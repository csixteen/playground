FROM golang:1.16 as builder
ENV GOPATH="/go"
WORKDIR /go/src/myapp
COPY . .
RUN make

FROM alpine:latest

LABEL maintainer="Pedro Rodrigues <csixteen@protonmail.com>"
COPY --from=builder /go/src/myapp/myapp /bin/

EXPOSE 8000

CMD ["/bin/myapp"]
